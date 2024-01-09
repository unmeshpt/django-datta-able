from django.urls import path, re_path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
  path('add_product/', views.add_product, name='add_product'),  
  path('create_order/', views.create_order, name='create_order'),  
  path('orders/', views.orders, name='orders'),  
  path('new_order/', views.new_order, name='new_order'),
  path('delete_addeditem/<id>/',views.delete_addeditem,name='delete_addeditem'),
  path('view_order/<id>/',views.view_order,name='view_order'),
  path('del_order/<id>/',views.del_order,name='del_order'),
  
  
]
