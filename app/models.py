from django.db import models

# Create your models here.

class model1(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    registration_no = models.PositiveIntegerField(unique=True,null=True)
    full_name = models.CharField(max_length=100,null=True)
    image = models.ImageField(upload_to='employee_images',blank=True)
    date_of_birth = models.DateField(verbose_name="Date of Birth", blank=True, null=True)
    department = models.CharField(max_length=100,null=True)
    age = models.IntegerField(null=True,max_length=100)
    phone_no = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    state = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=100,null=True)
    nationality = models.CharField(max_length=100,null=True)
    e_mail = models.EmailField(null=True) 

    def __str__(self):
        return self.full_name
