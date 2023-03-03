from django.db import models
# Create your models here.


class Booking(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    people = models.IntegerField()
    special_requirements = models.TextField()
    date = models.DateField()
    time = models.TimeField()
