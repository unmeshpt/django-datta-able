from django.apps import apps
from django.contrib import admin

# Register your models here.

class ProductAdmin(admin.ModelAdmin):

    list_filter=['info']
    list_display=['id','name','info','price',]
    search_fields=['id','name','info','price']
    list_per_page=10

app_models = apps.get_app_config('home').get_models()
for model in app_models:
    try:  
        admin.site.register(model, ProductAdmin)
    except Exception:
        pass
