from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# Create your models here.


class Booking(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone must be entered in the format: '+999999999'.")

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="booking")
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(
        validators=[phone_regex],
        max_length=17,
        blank=True)
    people = models.IntegerField()
    special_requirements = models.TextField(blank=True)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name
