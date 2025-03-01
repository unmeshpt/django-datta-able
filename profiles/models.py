from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
        # Add more social media platforms as needed
    ]
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='user_profile')
    gender=models.CharField(max_length=10,  choices=GENDER, null=True)
    house_no=models.CharField(max_length=50,blank=True, null=True)
    street=models.CharField(max_length=50,blank=True, null=True)
    city=models.CharField(max_length=50,blank=True, null=True)
    state=models.CharField(max_length=50,blank=True, null=True)
    country=models.CharField(max_length=50,blank=True, null=True)
    zipcode=models.CharField(max_length=50,blank=True, null=True)
    bio=models.TextField(max_length=350, blank=True, null=True)
    phone= models.CharField(max_length=12, blank=True, null=True)
    dob=models.DateField(null=True)
    is_admin=models.BooleanField(default=False)
    profileimg=models.ImageField(upload_to='images/users/', null=True, blank=True)

    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.user}"

