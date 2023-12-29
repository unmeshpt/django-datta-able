from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.title

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Staff(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_staff')
    hire_date = models.DateField()
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, blank=True, related_name='staff_position')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, related_name='staff_department')
    
    def __str__(self):
        return f"{self.user}"