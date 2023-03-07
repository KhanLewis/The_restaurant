from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Booking(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booking")
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    people = models.IntegerField()
    special_requirements = models.TextField()
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name
