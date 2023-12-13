from django.urls import path
from .views import car, customer

urlpatterns = [
    path('car/', car.view_all_cars),
    path('car/add/', car.add_car),
    path('car/<int:car_pk>/', car.view_car_details),
    path('car/<int:car_pk>/active_booking/', car.view_car_details_active_booking),
    path('car/<int:car_pk>/update/', car.edit_car_details),
    path('car/<int:car_pk>/delete/', car.delete_car),

    path('', car.home),

    path('customer/', customer.view_all_customers),
    path('customer/add/', customer.add_customer),
    path('customer/<int:cust_pk>/', customer.view_customer_details),
    path('customer/<int:cust_pk>/update/', customer.edit_details),
    path('customer/<int:cust_pk>/delete/', customer.delete_customer),
]