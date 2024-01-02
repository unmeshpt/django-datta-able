from django.urls import path

from . import views

urlpatterns = [
  path('add_services/', views.add_services, name='add_services'),
]
