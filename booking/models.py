from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Booking(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="booking")

    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    people = models.IntegerField()
    special_requirements = models.TextField(blank=True)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name
