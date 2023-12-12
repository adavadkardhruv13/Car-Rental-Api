from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.serializers import (CarSerializer, ReservationSerializer, CarDetailsReservationSerializer, AvailableCarSerializer)
from car_api.models import Car, Reservation, Customer
from rest_framework import status
from collections import namedtuple
from datetime import datetime, date
from django.db.models import Q


# api for hone page
@api_view['GET']
def home(request):
    if request.method == 'GET':
        data = {'message':'Welcome to Car-Rental-Agency'}
        return JsonResponse(data, safe=False)


# api endpoint for getting all details of the car
@api_view['GET']
def view_all_cars(request):
    if request.method == 'GET':
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)


#api endpoint for getting the details of a perticular car
@api_view['GET']
def view_car_details(request, pk):
        try:
            details = Car.objects.all()
        except details.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = CarSerializer(details)
            return Response(serializer.data)

#api endpoint for displaying specific car details with its active reservation details

@api_view['GET']
def view_car_details_active_booking(request, pk):
    try:
        car = Car.objects.all()
    except car.DoesNotExsit:
        return Response(status= status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        current_date = date.today()
        CarBookingDetails = namedtuple('CarBookingDetails',('car', 'current_active_bookings'))

        condition_1 = Q(issue_data__gte = current_date)
        condition_2 = Q(return_data__gte = current_date)

        carBookingDetails = CarBookingDetails(
            car = car,
            current_active_bookings = Reservation.objects.all.filter(car).filter(condition_1 | condition_2)
        )

        serializer = CarDetailsReservationSerializer()
        return(serializer.data)


#api endpoint for adding a new car

@api_view['POST']
def add_car(request):
    if request.method == 'POST':
        serializer = CarSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

#api end
