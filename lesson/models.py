from django.db import models

# Create your models here.
# Tworzenie struktury bazy danych:
class Car (models.Model):
    producer = models.CharField(max_length= 32)
    model = models.CharField(max_length=32)
    seats = models.PositiveIntegerField()


