from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categories(models.Model):
    choices = [
        ('science', 'Science'),
        ('electrical', 'Electrical'),
        ('clothes', 'clothes'),
        ('watches', 'Watches'),
        ('handbag', 'Handbag'),
    ]
    
    category = models.CharField(max_length=30, choices=choices, default='science')

    def __str__(self):
        return str(self.category)





class Product(models.Model):
    category = models.ForeignKey(Categories, null=True, blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
