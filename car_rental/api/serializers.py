from rest_framework import serializers
from . models import Car, Customer, Reservation

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'phone']
class CarSerializer(serializers.ModelSerializer):
     class Meta:
        model = Car
        fields = ['id', 'vehicle_number', 'model', "seating_capacity", 'rent_per_day']


class AvailableCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'vehicle_number', 'model', "seating_capacity", 'rent_per_day','availability']

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['customer', 'car', 'issue_date', 'return_date']

class CarDetailReservationSerializer(serializers.ModelSerializer):
    car = CarSerializer()
    current_active_booking = ReservationSerializer(many=True)