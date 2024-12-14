
from django.urls import path

from cars import views



urlpatterns = [
    path('', views.home, name='home'),
    path('details/<int:id>', views.car_detail),
    path('delete/<int:id>', views.delete),
    path('create/', views.upload, name='create'),
    path('edit/<int:id>', views.edit),
]