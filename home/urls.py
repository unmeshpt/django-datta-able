from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
  path(''       , views.index,  name='index'),
  path('tables/', views.tables, name='tables'),
  path('order_approve/<pk>/', views.order_approve, name='order_approve'),
   path('order_completed/<pk>/', views.order_completed, name='order_completed'),
  path('order_reject/<pk>/', views.order_reject, name='order_reject'),
  path('order_cancel/<pk>/', views.order_cancel, name='order_cancel'),
  path('order_pending/<pk>/', views.order_pending, name='order_pending'),
]
