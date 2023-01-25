from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.forms import ModelForm,TextInput
# Create your views here.

class Product(models.Model):
    product_id = models.IntegerField(primary_key = True)
    product_name = models.CharField(max_length=255)
    product_image = models.ImageField(upload_to='media')
    product_price = models.CharField(max_length=500)
    product_url = models.URLField(blank=True)

class Cart(models.Model):
    cart_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(null=True)

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

            
        
        

        
        