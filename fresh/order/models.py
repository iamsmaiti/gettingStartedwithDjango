from django.db import models
from product.models import Item

# Create your models here.

#class Order(models.Model):
#    email = models.EmailField()


class OrderProduct(models.Model):
    items = models.ManyToManyField(Item, blank=True )
    total = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False )
    active = models.BooleanField(default=True)

    def __str__(self):
    	return "OrderProduct id: %s" %(self.id)
    
