from django.db import models

# Create your models here.
class Store(models.Model):
	name = models.CharField(max_length=20)
	address = models.CharField(max_length=200)
	lat = models.DecimalField(max_digits=8, decimal_places=2)
	lng = models.DecimalField(max_digits=8, decimal_places=2)
	
	def __str__(self):
		return self.name

