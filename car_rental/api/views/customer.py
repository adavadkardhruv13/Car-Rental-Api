from api.models import Customer
from api.serializers import CustomerSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

#api endpoint for showing all customers
@api_view(['GET'])
def view_all_customers(request):
    if request.method == 'GET':
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#api endpoint to show a specifice customer
@api_view(['GET'])
def view_customer_details(request, cust_pk):

        try:
            customer = Customer.objects.get(pk=cust_pk)
        except Customer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)

#endpoint for adding a new customer
@api_view(['POST'])
def add_customer(request):
    if request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#api endpoint for editing specific customer details
@api_view(['PUT'])
def edit_details(request, cust_pk):
    try:
        customer = Customer.objects.get(pk=cust_pk)
    except Customer.DoesNotExist():
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CustomerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#api endpoints for deleting a perticular customer
@api_view(['DELETE'])
def delete_customer(request, cust_pk):
    try:
        customer = Customer.objects.get(pk=cust_pk)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)