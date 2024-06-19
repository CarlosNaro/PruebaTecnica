from django.db import models
from django.db.models import Q


# Create your models here.

class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    plaque = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.brand} {self.model} {self.plaque}"


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    document = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Contract(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    weekly_fee = models.FloatField()

    @staticmethod
    def get_filtered_contracts(query=None):
        if query:
            contract_list = Contract.objects.prefetch_related('client', 'car').filter(
                Q(client__first_name__icontains=query) | Q(client__last_name__icontains=query) |
                Q(client__document__icontains=query) | Q(car__brand__icontains=query)
            )
        else:
            contract_list = Contract.objects.prefetch_related('client', 'car').all()
        return contract_list
