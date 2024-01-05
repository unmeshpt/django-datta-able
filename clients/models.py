from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NewOrder(models.Model):    
    STATUS = [
        ('New', 'New'),
        ('Active', 'Active'),
        ('Cancelled', 'Cancelled'),
        ('Pending', 'Pending'),
        ('Done', 'Done')
    ]    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='user_order')
    order_no = models.CharField(max_length=20, unique=True)
    project_name=models.CharField( max_length=50, null=True, blank=True)
    deadline=models.DateField()
    order_status= models.CharField(max_length=20, choices=STATUS)

    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    def __str__(self):
        return self.order_no
    
class OrderItem(models.Model):    
    new_order = models.ForeignKey(NewOrder, on_delete=models.CASCADE, related_name='new_order')
    item=models.CharField( max_length=50)
    description=models.TextField( max_length=350, null=True, blank=True)
    quantity=models.IntegerField()

    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    def __str__(self):
        return self.item
    
class LastOrderNo(models.Model):    
    order_no = models.CharField(max_length=20)
  
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    def __str__(self):
        return self.order_no