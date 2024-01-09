from django.urls import path, re_path
from . import views

urlpatterns = [
  path('add_product/', views.add_product, name='add_product'),  
  path('orders/', views.orders, name='orders'),  
  path('create_order/', views.create_order, name='create_order'),  
  path('new_order/', views.new_order, name='new_order'),
  path('delete_addeditem/<pk>/',views.delete_addeditem,name='delete_addeditem'),
  path('view_order/<pk>/',views.view_order,name='view_order'),
  path('del_order/<pk>/',views.del_order,name='del_order'),
  
  
]
