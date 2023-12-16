from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from api.serializers import (CarSerializer, ReservationSerializer, CarDetailReservationSerializer, AvailableCarSerializer)
from api.models import Car, Reservation, Customer
from rest_framework import status
from collections import namedtuple
from datetime import datetime, date
from django.db.models import Q
from rest_framework.parsers import JSONParser


# api for hone page
@api_view(['GET'])
def home(request):
    if request.method == 'GET':
        data = {'message':'Welcome to Car-Rental-Agency'}
        return JsonResponse(data, safe=False)


# api endpoint for getting all details of the car
@api_view(['GET'])
def view_all_cars(request):
    if request.method == 'GET':
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        print(f"Serialized Data: {serializer.data}")
        return Response(serializer.data)


#api endpoint for getting the details of a perticular car
@api_view(['GET'])
def car_details(request, pk):
        try:
            details = Car.objects.get(pk=pk)
        except details.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = CarSerializer(details)
            return Response(serializer.data)

#api endpoint for displaying specific car details with its active reservation details

@api_view(['GET'])
def view_car_details_with_active_booking(request, pk):
    try:
        car = Car.objects.get(by=pk)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        current_date = date.today()
        condition_1 = Q(issue_data__gte=current_date)
        condition_2 = Q(return_data__gte=current_date)

        carBookingDetails = namedtuple('CarBookingDetails', ('car', 'current_active_bookings'))
        carBookingDetails = carBookingDetails(
            car=car,
            current_active_bookings=Reservation.objects.all().filter(car).filter(condition_1 | condition_2)
        )

        serializer = CarDetailReservationSerializer(carBookingDetails)
        return Response(serializer.data)



#api endpoint for adding a new car

@api_view(['POST'])
def add_car(request):
    if request.method == 'POST':
        serializer = CarSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#api endpoint for editing a perticular car details
@api_view(['PUT'])
def edit_car_details(request, pk):
    try:
        car = Car.objects.get(by=pk)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#api endpoint for deleting a car
@api_view(['DELETE'])
def delete_car(request, pk):
    try:
        car = Car.objects.get(by=pk)
    except car.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



'''API endpoint for showing the cars with their availability status on a given date.
And filter the cars based on various fields.'''
@api_view(["GET"])
@parser_classes([JSONParser])
def view_all_cars_on_given_date(request):
    if request.method == 'GET':
        # Fetch date from url if passed or else set default to today's date.
        date_to_check = request.GET.get('date', str(date.today()))
        date_to_check = datetime.strptime(date_to_check, '%Y-%m-%d').date()  # Convert date to datetime format.

        # Fetch filters like model, capacity or availability status
        # if passed any as GET request URL parameters
        model = request.GET.get('model')
        capacity = request.GET.get('capacity')
        availability = request.GET.get('availability')

        # Filter all car reservations which falls in between date_to_check
        condition_1 = Q(issue_date__gte=date_to_check)
        condition_2 = Q(return_date__gte=date_to_check)
        reservations = Reservation.objects.filter(condition_1 | condition_2)
        serializer = ReservationSerializer(reservations, many=True)
        reservation_data = serializer.data

        # Get list of car ids which are reserved on the given date.
        occupied_car_id_lists = []
        for i in range(len(reservation_data)):
            occupied_car_id_lists.append(reservation_data[i]['car'])
        list_of_car_id = list(set(occupied_car_id_lists))

        # Setting availability of all car to True
        Car.objects.all().update(availability=True)

        # Setting availability of all reserved car to False
        for car_id in list_of_car_id:
            Car.objects.filter(id=car_id).update(availability=False)

        # Querying and filtering the cars based on various fields.
        cars = Car.objects.all()
        filters = {'model': model, 'seating_capacity': capacity, 'availability': availability}
        for key, value in filters.items():
            if value is not None:
                cars = cars.filter(**{key: value})
        car_serializer = AvailableCarSerializer(cars, many=True)

        return Response(car_serializer.data)