from django.db import models

# Create your models here.

class Students(models.Model):
    Name=models.CharField(max_length=100)
    reg=models.IntegerField(verbose_name="Register Number")
    dob=models.DateField(verbose_name="Date of Birth")
    Course=models.CharField(max_length=100)
    simage=models.ImageField(upload_to="students_image",verbose_name="students image")

