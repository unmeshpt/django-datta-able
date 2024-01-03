from django.db import models
from django.contrib.auth.models import User
from company.models import Company



class Department(models.Model):
    company=models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True, related_name='staff_department')
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Create your models here.
class Position(models.Model):
    department=models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, related_name='staff_position')
    title = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.title

class Staff(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_staff')
    hire_date = models.DateField()
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, blank=True, related_name='staff_position')
    
    def __str__(self):
        return f"{self.user}"