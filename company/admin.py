from django.contrib import admin
from .models import *

class ServicesAdmin(admin.ModelAdmin):
    list_filter=['service']
    list_display=['service','description']
    search_fields=['service']
    list_per_page=10

class ProductsAdmin(admin.ModelAdmin):
    list_filter=['services']
    list_display=['services','product','description']
    search_fields=['services']
    list_per_page=10



class CompanyAdmin(admin.ModelAdmin):
    list_filter=['business_name']
    list_display=['business_name','business_type']
    search_fields=['business_name']
    list_per_page=10

admin.site.register(Products, ProductsAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(BusinessType)


