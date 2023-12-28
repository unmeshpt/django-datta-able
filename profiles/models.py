from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='user_info')
    address=models.TextField(max_length=350,blank=True, null=True)
    bio=models.TextField(max_length=350, blank=True, null=True)
    phone= models.CharField(max_length=12, blank=True, null=True)
    profileimg=models.ImageField(upload_to='images/users/', null=True)

    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.user}"

# class CustomUser(AbstractUser):
#     id=models.IntegerField(primary_key=True)
#     username=models.CharField(unique=True, max_length=50)
#     dob=models.DateField()
#     hire_date=models.DateField()
#     phone= models.CharField(max_length=12, blank=True, null=True)
#     address=models.TextField(max_length=350,blank=True, null=True)
#     bio=models.TextField(max_length=350, blank=True, null=True)
#     date_joined=models.DateTimeField(auto_now_add=True)
#     is_staff=models.BooleanField(default=False)
#     is_active=models.BooleanField(default=True)
#     is_superuser=models.BooleanField(default=False)
#     is_admin=models.BooleanField(default= False)
#     last_login=models.DateTimeField(blank=True, null=True)
#     profileimg=models.ImageField(upload_to='images/users/', null=True)

    

#     def __str__(self):
#         return self.user_ptr

