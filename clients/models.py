from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import os

# Create your models here.
def custom_upload_to(instance, filename):
    """Custom function to change the filename of uploaded files."""
    neworder = NewOrder.objects.filter(user=instance.user, order_status='New').first()
    ext = filename.split('.')[-1]  # Get the file extension
    new_filename = f"{neworder.order_no}.{ext}"  # Generate a new filename using UUID4
    return os.path.join('files/order_files/', new_filename)  # You can customize the directory structure

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
    assets=models.ImageField(upload_to=custom_upload_to, null=True, blank=True)

    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    def __str__(self):
        return self.order_no
    
    def delete(self, *args, **kwargs):
        # Delete the file associated with the instance
        self.assets.delete()

        # Call the base class delete() method to delete the model instance
        super().delete(*args, **kwargs)

def generate_order_number():
    current_date = timezone.now().strftime('%Y')
    current_year=str(current_date)[-2:]
    last_order = NewOrder.objects.all().order_by('-order_no').first()
   
    if last_order:
        counter = int(last_order.order_no[-7:]) + 1
    else:
        counter = 1

    return f"ORD-{current_year}-{counter:07d}"

    
class OrderItem(models.Model):    
    new_order = models.ForeignKey(NewOrder, on_delete=models.CASCADE, related_name='neworder')
    item=models.CharField( max_length=50)
    description=models.TextField( max_length=350, null=True, blank=True)
    quantity=models.IntegerField()

    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    def __str__(self):
        return self.item
    

