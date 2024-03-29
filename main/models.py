from django.db import models
from django.utils import timezone


class Building(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Floor(models.Model):
    number = models.IntegerField()
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    def __int__(self):
        return self.number


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Object(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=250)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)

    def __int__(self):
        return self.number


class Item(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(Item, self).save(*args, **kwargs)

    def __str__(self):
        return self.object.name


class TelegramUser(models.Model):
    name = models.CharField(max_length=250)
    telegram_id = models.CharField(max_length=250)

    def __str__(self):
        return self.name