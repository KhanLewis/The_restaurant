from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DeleteView, View, TemplateView
from django.views.generic.edit import UpdateView
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Booking
from .forms import BookingForm

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
        form = BookingForm(data=request.POST)
        form.instance.owner = request.user
        if form.is_valid():
            bookings = Booking.objects.filter(
                owner=request.user,
                date=form.instance.date,
                time=form.instance.time)
            if (len(bookings) > 0):
                messages.add_message(
                    request,
                    messages.ERROR,
                    'This booking is not available')
            else:
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
    form = BookingForm
    template_name = 'update_booking.html'

    def get(self, request, pk, *args, **kwargs):
        form = self.form(data=request.POST)
        booking = Booking.objects.get(pk=pk)
        form = BookingForm(instance=booking)

        return render(request, self.template_name, {'form': form})

    def post(self, request, pk, *args, **kwargs):
        booking = Booking.objects.get(pk=pk)
        form = BookingForm(data=request.POST, instance=booking)
        form.instance.owner = request.user
        if form.is_valid():
            bookings = Booking.objects.filter(
                owner=request.user,
                date=form.instance.date,
                time=form.instance.time).exclude(pk=pk)
            if (len(bookings) > 0):
                messages.add_message(
                    request,
                    messages.ERROR,
                    'This booking is not available')
            else:
                form.save()
                return HttpResponseRedirect('/mybooking/')

        return render(request, self.template_name, {'form': form})


class DeleteBooking(DeleteView):
    model = Booking
    template_name = 'delete_booking.html'

    def delete(self, request, pk, *args, **kwargs):
        user = request.user
        exsiting_booking = get_object_or_404(Booking, pk=pk, owner=user)
        exsiting_booking.delete()
        return HttpResponseRedirect('/mybooking/')


class MenuView(ListView):

    model = Booking
    template_name = "menu.html"
