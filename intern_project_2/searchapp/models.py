from django.db import models

# Create your models here.
class Transport(models.Model):
    vehicle = models.TextField(blank=True, null=True)  # This field type is a guess.
    carrier = models.FloatField(blank=True, null=True)
    location_no = models.FloatField(blank=True, null=True)
    mcmu = models.FloatField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)  # This field type is a guess.
    customer_code = models.FloatField(blank=True, null=True, unique=True)
    zone = models.TextField(blank=True, null=True)  # This field type is a guess.
    quantity = models.FloatField(blank=True, null=True)
    rtkm = models.FloatField(blank=True, null=True)
    klkm = models.FloatField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    load = models.FloatField(blank=True, null=True)
    capacity = models.FloatField(blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
