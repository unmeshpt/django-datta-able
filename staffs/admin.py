from django.apps import apps
from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.

# Register your models here.
class StaffAdmin(admin.ModelAdmin):
    list_filter=['Current_Status']
    list_display=['first_name','position','department','email','phone_number', 'status','_']
    search_fields=['first_name','last_name','position', "status"]
    list_per_page=10


    #Function to change the icons
    def _(self,obj):
        if obj.Current_Status=='Active':
            return True
        elif obj.Current_Status=='Pending':
            return None
        else:
            return False
    _.boolean = True   

    #Function to color the text
    def status(self, obj):
        if obj.Current_Status=='Active':
            color='#28a745'
        elif obj.Current_Status=='Pending':
            color='#fea95e'
        else:
            color='red'
        return format_html('<strong><p style="color:{}">{}</p></strong>'.format(color, obj.Current_Status))
    status.allow_tags=True


app_models = apps.get_app_config('staffs').get_models()
for model in app_models:
    try:    
        if (model.__name__ == "Staff") :
            admin.site.register(model, StaffAdmin)
        else: 
            admin.site.register(model)


    except Exception:
        pass
