from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_name = models.CharField(max_length= 50)
    customer_phone = models.CharField(max_length= 20)
    customer_mail = models.CharField(max_length= 100)
    customer_image = models.ImageField(upload_to='customer/')
    customer_password = models.CharField(max_length=15)
    customer_addres = models.CharField(max_length= 500)

    class Meta:
        db_table ='customer_tb'

class Seller(models.Model):
    seller_first_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    mail = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='seller/')
    ac_number = models.BigIntegerField()
    ifsc = models.CharField(max_length=20)
    account_holder = models.CharField(max_length=30)
    branch = models.CharField(max_length=30)
    address = models.CharField(max_length=500)
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        db_table ='seller_tb'
