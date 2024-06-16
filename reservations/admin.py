from django.contrib import admin
from reservations.models import Bike, Reservation

# Register your models here.
class BikeAdmin (admin.ModelAdmin):
    fields = ["name_bike", "price_bike"]
    list_display = ["name_bike", "price_bike", "is_reservated"]

class ReservationAdmin(admin.ModelAdmin):
    fields = ["data_created", "bike", "start_reserve", "end_reserve"]
    readonly_fields = ["data_created",]
    list_display = ["data_created", "bike", "start_reserve", "end_reserve"]


admin.site.register(Bike, BikeAdmin)
admin.site.register(Reservation, ReservationAdmin)
