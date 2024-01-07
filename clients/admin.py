from django.contrib import admin
from .models import *


class NewOrderAdmin(admin.ModelAdmin):
    list_filter=['user']
    list_display=['user','order_no','project_name','deadline', 'order_status', 'assets']
    search_fields=['deadline', 'order_status']
    list_per_page=10


class OrderItemAdmin(admin.ModelAdmin):
    list_filter=['new_order']
    list_display=['new_order','item','description','quantity']
    search_fields=['new_order','item',]
    list_per_page=10



class CompanyAdmin(admin.ModelAdmin):
    list_filter=['business_name']
    list_display=['business_name','business_type']
    search_fields=['business_name']
    list_per_page=10

admin.site.register(NewOrder, NewOrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)


