from api.models import Reservation
from api.serializers import ReservationSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from datetime import date

#api endpoint for getting all the reservation
@api_view(['GET'])
def view_all_reservation(request):
    if request.method == 'GET':
        reservation = Reservation.objects.all()
        serializer = ReservationSerializer(reservation, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#api endpoint for booking a car
@api_view(['POST'])
def add_booking(request):
    if request.method == 'POST':
        serializer = ReservationSerializer(data=request.data)

        if serializer.is_valid():
            issue_date = serializer.validate_data['issue_date']
            return_date = serializer.validate_data['return_date']

            car = serializer.validate_data['car']
            reservation = Reservation.objects.filter(car=car.id)

            current_date = date.today()
            for r in reservation:
                if r.issue_data <= issue_date <= return_date:
                    content = {'message': 'The car selected in not avaliable on this date'}
                    return Response(content, status=status.HTTP_400_BAD_REQUEST)

            if current_date<=issue_date and issue_date<=return_date:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#api endpoint for updating the reservation details
@api_view(['PUT'])
def edit_reservation(request, pk):
    try:
        reservation = Reservation.objects.get(pk=pk)
    except Reservation.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'PUT':
        serializer = ReservationSerializer(reservation, data= request.data)

        if serializer.is_valid():
            issue_date = serializer.validate_data['issue_date']
            return_date = serializer.validate_data['return_date']
            car = serializer.validate_data['car']
            reservation = Reservation.objects.filter(car=car.id)

            current_date = date.today()
            for r in reservation:
                if r.issue_date <= return_date <= r.return_date:
                    content = {"message": "Failed to extend the date. Car is not available."}
                    return Response(content, status=status.HTTP_400_BAD_REQUEST)

            if current_date <= issue_date and issue_date <= return_date:
                serializer.save()
                return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#api endpoint for getting all details of the reservation
@api_view(['GET'])
def view_reservation_details(request, pk):
    """
    API endpoint for showing a particular reservation details.
    """
    try:
        reservation = Reservation.objects.get(pk=pk)
    except Reservation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data)

#api endpoint to delete the reservation
@api_view(['DELETE'])
def cancel_reservation(request,pk):
    """
    API endpoint for cancelling a specific Booking.
    """
    try:
        reservation = Reservation.objects.get(pk=pk)
    except Reservation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        reservation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

