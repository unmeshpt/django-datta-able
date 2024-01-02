from django.urls import path

from . import views

urlpatterns = [
  path('new_order/', views.new_order, name='new_order'),
]
