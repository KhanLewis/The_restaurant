from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DeleteView, View, TemplateView
from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect
from .models import Booking
from .forms import BookingForm
from django.urls import reverse_lazy
# Create your views here.


class HomepageView(ListView):
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
        form.instance.owner = request.user
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/mybooking/')

        return render(request, self.template_name, {'form': form})


class MyBookingView(ListView):

    def get(self, request, *args, **kwargs):
        queryset = Booking.objects.filter(owner=request.user)
        booking = queryset

        return render(
            request,
            "view_booking.html",
            {
                "bookings": booking,
            },
        )


class BookingUpdateView(TemplateView):

    model = Booking
    template_name = 'update_booking.html'

    def get(self, request, pk, *args, **kwargs):
   
        booking = Booking.objects.get(pk=pk)
        form = BookingForm(instance=booking)

        return render(request, self.template_name, {'form': form})

    def post(self, request, pk, *args, **kwargs):

        booking = Booking.objects.get(pk=pk)
        form = BookingForm(data=request.POST, instance=booking)
        form.instance.owner = request.user

        if form.is_valid():
            form.save()
            form.instance.owner = request.user
            booking = form.save(commit=False)
            booking.save()
            return HttpResponseRedirect('/mybooking/')

        return render(request, self.template_name, {'form': form})


class DeleteBooking(DeleteView):
    model = Booking
    template_name = 'delete_booking.html'
    
    def delete(self, request, pk, *args, **kwargs):
        exsiting_booking = get_object_or_404(Booking, pk=pk)
        exsiting_booking.delete()
        return HttpResponseRedirect('/mybooking/')


class MenuView(ListView):

    model = Booking
    template_name = "menu.html"
