from django.shortcuts import render
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Booking
from .forms import BookingForm
# Create your views here.


class HomepageView(generic.ListView):
    model = Booking
    template_name = "index.html"


class MakeBookingView(View):
    form = BookingForm
    template_name = 'booking.html'

    def get(self, request, *args, **kwargs):
        form = self.form()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/mybooking/')

        return render(request, self.template_name, {'form': form})


class MyBookingView(generic.ListView):

    def get(self, request, *args, **kwargs):
        queryset = Booking.objects.filter(owner=request.user)
        booking = queryset

        return render(
            request,
            "view_booking.html",
            {
                "booking": booking,
            },
        )


class MenuView(generic.ListView):

    model = Booking
    template_name = "menu.html"
