from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='user_profile')
    address=models.TextField(max_length=350,blank=True, null=True)
    bio=models.TextField(max_length=350, blank=True, null=True)
    phone= models.CharField(max_length=12, blank=True, null=True)
    profileimg=models.ImageField(upload_to='images/users/', null=True)

    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.user}"
