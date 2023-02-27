from django.db import models

from commen.models import Seller

# Create your models here.

class Product(models.Model):
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE)
    product_id = models.CharField(max_length=100)
    product_name =models.CharField(max_length=100)
    discription =  models.CharField(max_length=500)
    stock = models.BigIntegerField()
    price = models.BigIntegerField()
    image = models.ImageField(upload_to='product/')

    class meta:
        db_table = 'product'