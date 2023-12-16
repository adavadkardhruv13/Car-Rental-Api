from django.urls import path
from .views import car, customer,reservation

urlpatterns = [
    path('car/', car.view_all_cars),
    path('car/add/', car.add_car),
    path('car/<int:pk>/', car.car_details),
    path('car/<int:pk>/active_booking/', car.view_car_details_with_active_booking),
    path('car/<int:pk>/update/', car.edit_car_details),
    path('car/<int:pk>/delete/', car.delete_car),
    path('car/status/', car.view_all_cars_on_given_date),
    path('', car.home),

    path('customer/', customer.view_all_customers),
    path('customer/add/', customer.add_customer),
    path('customer/<int:cust_pk>/', customer.view_customer_details),
    path('customer/<int:cust_pk>/update/', customer.edit_details),
    path('customer/<int:cust_pk>/delete/', customer.delete_customer),

    path('rent/', reservation.all_reservation),
    path('rent/book/', reservation.add_booking),
    path('rent/<int:pk>/', reservation.view_reservation_details),
    path('rent/<int:pk>/update/', reservation.edit_reservation),
    path('rent/<int:pk>/delete/', reservation.cancel_reservation),

]