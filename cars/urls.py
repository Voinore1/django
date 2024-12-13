
from django.urls import path

from cars import views



urlpatterns = [
    path('', views.home),
    path('details/<int:id>', views.car_detail),
]