from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomepageView.as_view(), name='home'),
    path('booking/', views.MakeBookingView.as_view(), name='booking'),
    path('mybooking/', views.MyBookingView.as_view(), name='my_booking'),
    path('updatebooking/<int:pk>', views.BookingUpdateView.as_view(), name='update_booking'),
    path('deletebooking/<int:pk>', views.DeleteBooking.as_view(), name='delete_booking'),
    path('menu/', views.MenuView.as_view(), name='menu'),
]
