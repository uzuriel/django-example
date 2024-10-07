from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    expiration_date = models.DateField(auto_now=False, auto_now_add=False)