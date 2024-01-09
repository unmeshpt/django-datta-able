from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_filter=['user']
    list_display=['user','house_no','street','city', 'state','country', 'zipcode', 'phone','profileimg','bio']
    search_fields=['user','phone']
    list_per_page=10

admin.site.register(Profile, ProfileAdmin)