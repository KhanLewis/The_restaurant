from django.contrib import admin
from .models import Booking
# Register your models here.


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ['name', 'date']
    list_filter = ('name', 'date', 'time')
