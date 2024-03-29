from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            usr = authenticate(username=username, password=password)
            if usr is not None:
                login(request, usr)
                return redirect('index')
            else:
                messages.warning(request, 'Username or password is wrong')
        else:
            print('ssssssssssss')
            messages.warning(request, 'No user found')
            return redirect('login')
    return render(request, 'sign-in.html')


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def index_view(request):
    context = {
        "buildings": Building.objects.all().count(),
        "floors": Floor.objects.all().count(),
        "categories": Category.objects.all().count(),
        "objects": Object.objects.all().count(),
        "rooms": Room.objects.all().count(),
        "items": Item.objects.all().count(),
        'telegram_users': TelegramUser.objects.all().count()
    }
    return render(request, 'index.html', context)


def page_not_found_view(request, exception):
    return render(request, 'error.html')


@login_required(login_url='login')
def settings(request):
    if request.method == "POST":
        user = request.user
        username = request.POST.get("username")
        password = request.POST.get("password")
        if User.objects.exclude(id=user.id).filter(username=username).exists():
            messages.warning(request, 'This username is busy!')
            return redirect('settings')
        user.username = username
        if password != "":
            user.set_password(password)
        user.save()
        login(request, user)
        return redirect('settings')
    return render(request, 'settings.html')


@login_required(login_url='login')
def buildings(request):
    context = {
        "buildings": Building.objects.all().order_by('-id')
    }
    return render(request, 'building.html', context)


@login_required(login_url='login')
def floors(request):
    context = {
        "floors": Floor.objects.all().order_by('-id')
    }
    return render(request, 'floors.html', context)


@login_required(login_url='login')
def rooms(request):
    context = {
        "rooms": Room.objects.all().order_by('-id')
    }
    return render(request, 'rooms.html', context)


@login_required(login_url='login')
def objects(request):
    context = {
        "objects": Object.objects.all().order_by('-id')
    }
    return render(request, 'objects.html', context)


@login_required(login_url='login')
def categories(request):
    context = {
        "categories": Category.objects.all().order_by('-id')
    }
    return render(request, 'categories.html', context)


@login_required(login_url='login')
def items(request):
    context = {
        "items": Item.objects.all().order_by('-id')
    }
    return render(request, 'items.html', context)


@login_required(login_url='login')
def building_delete(request, pk):
    Building.objects.get(id=pk).delete()
    return redirect('buildings')


@login_required(login_url='login')
def category_delete(request, pk):
    Category.objects.get(id=pk).delete()
    return redirect('categories')


@login_required(login_url='login')
def floor_delete(request, pk):
    Floor.objects.get(id=pk).delete()
    return redirect('floors')


@login_required(login_url='login')
def item_delete(request, pk):
    Item.objects.get(id=pk).delete()
    return redirect('items')


@login_required(login_url='login')
def object_delete(request, pk):
    Object.objects.get(id=pk).delete()
    return redirect('objects')


@login_required(login_url='login')
def room_delete(request, pk):
    Room.objects.get(id=pk).delete()
    return redirect('rooms')


@login_required(login_url='login')
def building_update(request, pk):
    building = Building.objects.get(id=pk)
    if request.method == 'POST':
        building.name = request.POST['name']
        building.save()
        return redirect('buildings')
    context = {
        "building": building
    }
    return render(request, 'building_update.html', context)


@login_required(login_url='login')
def category_update(request, pk):
    category = Category.objects.get(id=pk)
    if request.method == 'POST':
        category.name = request.POST['name']
        category.save()
        return redirect('categories')
    context = {
        "category": category
    }
    return render(request, 'category_update.html', context)


@login_required(login_url='login')
def floor_update(request, pk):
    floor = Floor.objects.get(id=pk)
    if request.method == 'POST':
        floor.number = request.POST['number']
        floor.building_id = request.POST['building']
        floor.save()
        return redirect('floors')
    context = {
        "buildings": Building.objects.all().order_by('-id'),
        'floor': floor
    }
    return render(request, 'floor_update.html', context)


@login_required(login_url='login')
def item_update(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == 'POST':
        item.room_id = request.POST['room']
        item.object_id = request.POST['object']
        item.quantity = request.POST['quantity']
        item.save()
        return redirect('items')
    context = {
        "rooms": Room.objects.all().order_by('-id'),
        'objects': Object.objects.all().order_by('-id'),
        "item": item
    }
    return render(request, 'item_update.html', context)


@login_required(login_url='login')
def object_update(request, pk):
    object1 = Object.objects.get(id=pk)
    if request.method == 'POST':
        object1.category_id = request.POST['category']
        object1.name = request.POST['name']
        object1.save()
        return redirect('objects')
    context = {
        "categories": Category.objects.all().order_by('-id'),
        'object': object1
    }
    return render(request, 'object_update.html', context)


@login_required(login_url='login')
def room_update(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.floor_id = request.POST['floor']
        room.name = request.POST['name']
        room.save()
        return redirect('rooms')
    context = {
        "floors": Floor.objects.all().order_by('-id'),
        "room": room
    }
    return render(request, 'room_update.html', context)


@login_required(login_url='login')
def building_create(request):
    if request.method == 'POST':
        Building.objects.create(
            name=request.POST['name']
        )
        return redirect('buildings')
    return render(request, 'building_create.html')


@login_required(login_url='login')
def category_create(request):
    if request.method == 'POST':
        Category.objects.create(
            name=request.POST['name']
        )
        return redirect('categories')
    return render(request, 'category_create.html')


@login_required(login_url='login')
def floor_create(request):
    if request.method == 'POST':
        Floor.objects.create(
            number=request.POST['number'],
            building_id=request.POST['building']
        )
        return redirect('floors')
    context = {
        "buildings": Building.objects.all().order_by('-id')
    }
    return render(request, 'floor_create.html', context)


@login_required(login_url='login')
def item_create(request):
    if request.method == 'POST':
        Item.objects.create(
            room_id=request.POST['room'],
            object_id=request.POST['object'],
            quantity=request.POST['quantity']
        )
        return redirect('items')
    context = {
        "rooms": Room.objects.all().order_by('-id'),
        'objects': Object.objects.all().order_by('-id'),
    }
    return render(request, 'item_create.html', context)


@login_required(login_url='login')
def object_create(request):
    if request.method == 'POST':
        Object.objects.create(
            category_id=request.POST['category'],
            name=request.POST['name']
        )
        return redirect('objects')
    context = {
        "categories": Category.objects.all().order_by('-id')
    }
    return render(request, 'object_create.html', context)


@login_required(login_url='login')
def room_create(request):
    if request.method == 'POST':
        Room.objects.create(
            floor_id=request.POST['floor'],
            name=request.POST['name']
        )
        return redirect('rooms')
    context = {
        "floors": Floor.objects.all().order_by('-id')
    }
    return render(request, 'room_create.html', context)


@login_required(login_url='login')
def building_details(request, pk):
    building = Building.objects.get(id=pk)
    floors = Floor.objects.filter(building=building)
    context = {
        "building": building,
        'floors': floors
    }
    return render(request, 'building_details.html', context)


@login_required(login_url='login')
def floor_details(request, pk):
    floor = Floor.objects.get(id=pk)
    rooms = Room.objects.filter(floor=floor)
    context = {
        "floor": floor,
        'rooms': rooms
    }
    return render(request, 'floor_details.html', context)


@login_required(login_url='login')
def room_details(request, pk):
    room = Room.objects.get(id=pk)
    items = Item.objects.filter(room=room)
    context = {
        "room": room,
        'items': items
    }
    return render(request, 'room_details.html', context)


@login_required(login_url='login')
def telegram_users(request):
    telegram_users = TelegramUser.objects.all()
    context = {
        "telegram_users": telegram_users
    }
    return render(request, 'telegram_users.html', context)


@login_required(login_url='login')
def telegram_user_create(request):
    if request.method == 'POST':
        TelegramUser.objects.create(
            name=request.POST['name'],
            telegram_id=request.POST['telegram_id']
        )
        return redirect('telegram_users')
    return render(request, 'telegram_user_create.html')


@login_required(login_url='login')
def telegram_user_update(request, pk):
    telegram_user = TelegramUser.objects.get(id=pk)
    if request.method == 'POST':
        telegram_user.name = request.POST['name']
        telegram_user.telegram_id = request.POST['telegram_id']
        telegram_user.save()
        return redirect('telegram_users')
    context = {
        "telegram_user": telegram_user
    }
    return render(request, 'telegram_user_update.html', context)


@login_required(login_url='login')
def telegram_user_delete(request, pk):
    TelegramUser.objects.get(id=pk).delete()
    return redirect('telegram_users')

