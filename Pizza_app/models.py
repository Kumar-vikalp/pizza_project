from django.db import models

# Create your models here.
class Register(models.Model):
    name=models.TextField()
    email=models.CharField(max_length=100)
    paswd=models.CharField(max_length=100)
    conf_paswd=models.CharField(max_length=100)

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=20)  # E.g., Veg/Non-veg
    size = models.CharField(max_length=10, null=True, blank=True)
    pizza_picture = models.ImageField(upload_to='pizza_pics/', null=True, blank=True)
