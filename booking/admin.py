from django.contrib import admin
from .models import Booking
# Register your models here.


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'email', 'phone')
    search_fields = ['owner', 'date']
    list_filter = ('owner', 'date', 'time')
