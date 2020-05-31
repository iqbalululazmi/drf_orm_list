from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    customer = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE,
        related_name='vehicle'
    )

    def __str__(self):
        return self.name
