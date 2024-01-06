from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

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
    
def generate_order_number():
    current_date = timezone.now().strftime('%Y')
    current_year=str(current_date)[-2:]
    last_order = NewOrder.objects.all().order_by('-order_no').first()
   
    if last_order:
        counter = int(last_order.order_no[-7:]) + 1
    else:
        counter = 1

    return f"ORD/{current_year}-{counter:07d}"
    
class OrderItem(models.Model):    
    new_order = models.ForeignKey(NewOrder, on_delete=models.CASCADE, related_name='neworder')
    item=models.CharField( max_length=50)
    description=models.TextField( max_length=350, null=True, blank=True)
    quantity=models.IntegerField()

    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    def __str__(self):
        return self.item
    

