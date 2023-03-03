from django.shortcuts import render
from django.views import generic
from .models import Booking
# Create your views here.


class HomepageView(generic.ListView):
    model = Booking
    template_name = "index.html"

