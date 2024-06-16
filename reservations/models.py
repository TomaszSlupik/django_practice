from django.db import models
from datetime import datetime, date

# Create your models here.

# 
class Bike(models.Model):
    name_bike = models.CharField(max_length=50)
    price_bike = models.PositiveIntegerField(default=0)

    @property
    def is_reservated(self):
        today = date.today()
        return self.reservation_set.filter(start_reserve__lte=today, end_reserve__gte=today).exists()

    def __str__(self) -> str:
        return f"{self.name_bike}"
    

class Reservation(models.Model):
    data_created = models.DateTimeField(auto_now_add=True)
    bike = models.ForeignKey(Bike, on_delete=models.PROTECT)
    start_reserve = models.DateField(default=datetime.now)
    end_reserve = models.DateField(default=datetime.now)

    def __str__(self) -> str:
        return f"Rezerwacja {self.data_created} rower: {self.bike}"




