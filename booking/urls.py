from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomepageView.as_view(), name='home'),
    path('booking/', views.MakeBookingView.as_view(), name='booking'),
    path('mybooking/', views.MyBookingView.as_view(), name='my_booking'),
    path('menu/', views.MenuView.as_view(), name='menu'),
]
