from django.db.models.deletion import CASCADE
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(null=True,blank=True)
    image_url = models.CharField(max_length=250)
    price = models.FloatField(null=True,blank=True)


    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, max_length=250, null=True,blank=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name