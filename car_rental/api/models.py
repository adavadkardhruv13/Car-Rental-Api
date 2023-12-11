from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=1000, unique=True)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return self.name

class Car(models.Model):
    vehicle_number = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    seating_capacity = models.IntegerField()
    rent_per_day = models.IntegerField()
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.model


class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car =  models.ForeignKey(Car, on_delete=models.CASCADE)
    issue_date = models.DateField()
    return_date = models.DateField()

    def __str__(self):
        return str(self.customer) + " " + str(self.car)