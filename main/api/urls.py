from django.urls import path
from .views import *


urlpatterns = [
    path('get_buildings/', get_buildings),
    path('get_building_by_id/<int:pk>/', get_building_by_id),
    path('get_floors_by_building/<int:pk>/', get_floors_by_building),
    path('get_rooms_by_floor/<int:pk>/', get_rooms_by_floor),
    path('get_categories/', get_categories),
    path('get_items_by_room/<int:pk>/', get_items_by_room),
    path('check_telegram_user_by_id/', check_telegram_user_by_id),
    path('get_categories_of_all_items_by_room/<int:pk>/', get_categories_of_all_items_by_room)
]