from django.urls import path
from .views import car

urlpatterns = [
    path('car/', car.view_all_cars),
    path('car/add/', car.add_car), # API 1: Add new cars
    path('car/<int:car_pk>/', car.view_car_details),
    path('car/<int:car_pk>/active_booking/', car.view_car_details_active_booking), # API 3: Show details of car with booking details
    path('car/<int:car_pk>/update/', car.edit_car_details),
    path('car/<int:car_pk>/delete/', car.delete_car),
]