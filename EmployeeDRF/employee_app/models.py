from django.db import models

from employee_app.choice import departmeny_choices


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.IntegerField(choices=departmeny_choices,default=1)
    salary = models.DecimalField(max_digits=10,decimal_places=2)
    data_joined=models.DateField(auto_now_add=True)
    profile_pic =models.FileField(upload_to='uploads/')

