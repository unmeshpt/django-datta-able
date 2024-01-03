from django.urls import path
from . import views 

from . import views

urlpatterns = [
  path('liststaffs/', views.list_staff, name='liststaffs'),
]
