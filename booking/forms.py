from .models import Booking
from django.forms import ModelForm, widgets


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ('__all__')
        exclude = ('owner',)
        widgets = {
            'date': widgets.DateInput(attrs={'type': 'date'}),
            'time': widgets.DateInput(attrs={'type': 'time'})
        }
