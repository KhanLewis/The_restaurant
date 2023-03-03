from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomepageView.as_view(), name='home')
]
