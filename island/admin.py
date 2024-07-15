from django.contrib import admin
from .models import *

class PlatAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "bio", "type","time","serve","price")

admin.site.register(Plat, PlatAdmin)


class ReservationAdmin(admin.ModelAdmin):
    list_display = ("id", "name","created_at", "phone", "email","time","serve","date")

admin.site.register(Reservation, ReservationAdmin)