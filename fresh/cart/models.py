from django.db import models
from user.models import User
from product.models import Item

# Create your models here.
class Address(models.Model):
	date_created = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey('auth.User',on_delete=models.CASCADE, related_name="addresses")
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	street_address1 = models.CharField(max_length=255)
	street_address2 = models.CharField(max_length=255, blank=True, null=True)
	city = models.CharField(max_length=25)
	state = models.CharField(max_length=25)
	zip = models.CharField(max_length=10)
	phone = models.IntegerField()

class Cart(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE, related_name="carts")
    items = models.ManyToManyField(Item)

class Order(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE, blank=True, null=True)
    items = models.ManyToManyField(Item) 
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE, related_name="orders")
    