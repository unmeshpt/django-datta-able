from django.db import models

STATUS=(
    ('pending','Pending'),
    ('active','Active'),
    ('inactive','Inactive'),
)

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
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    hire_date = models.DateField()
    position = models.OneToOneField(Position, on_delete=models.SET_NULL, null=True, blank=True, related_name='staff_position',)
    department = models.OneToOneField(Department, on_delete=models.SET_NULL, null=True, blank=True, related_name='staff_department', )
    staff_image = models.ImageField(upload_to='files/staff_assets/staff_photos')
    Current_Status = models.CharField( max_length=50,null=True,choices=STATUS,default='pending')
    def __str__(self):
        return f"{self.first_name} {self.last_name}"