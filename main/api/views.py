from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import *
from .serializer import *
from rest_framework.status import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR


@api_view(['GET'])
def get_buildings(request):
    buildings = Building.objects.all().order_by('-id')
    data = BuildingSerializer(buildings, many=True).data
    return Response(data)


@api_view(['GET'])
def get_building_by_id(request, pk):
    building = Building.objects.get(id=pk)
    data = BuildingSerializer(building).data
    return Response(data)


@api_view(['GET'])
def get_floors_by_building(request, pk):
    building = Building.objects.get(id=pk)
    floors = Floor.objects.filter(building=building)
    data = FloorSerializer(floors, many=True).data
    return Response(data)


@api_view(['GET'])
def get_rooms_by_floor(request, pk):
    floor = Floor.objects.get(id=pk)
    rooms = Room.objects.filter(floor=floor)
    data = RoomSerializer(rooms, many=True).data
    return Response(data)


@api_view(['GET'])
def get_categories(request):
    data = CategorySerializer(Category.objects.all().order_by('-id'), many=True).data
    return Response(data)


@api_view(['GET'])
def get_items_by_room(request, pk):
    room = Room.objects.get(id=pk)
    data = ItemSerializer(Item.objects.filter(room=room), many=True).data
    return Response(data)


@api_view(['GET'])
def check_telegram_user_by_id(request):
    telegram_id = request.GET['telegram_id']
    if TelegramUser.objects.filter(telegram_id=telegram_id).exists():
        status = HTTP_200_OK
        data = {
            "message": "You are allowed to use this bot"
        }
    else:
        status = HTTP_500_INTERNAL_SERVER_ERROR
        data = {
            "message": "You are not allowed to use this bot"
        }
    return Response(data, status=status)


@api_view(['GET'])
def get_categories_of_all_items_by_room(request, pk):
    room = Room.objects.get(id=pk)
    category = Category.objects.filter(object__item__room=room)
    data = CategorySerializer(category, many=True).data
    return Response(data)


