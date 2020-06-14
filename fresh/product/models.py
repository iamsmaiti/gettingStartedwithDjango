from django.db import models

# Create your models here.

#item model defined
class Item(models.Model):
	title = models.CharField(max_length=20)
	descripyion = models.TextField(max_length=200)
	category = models.CharField(max_length=10)
	price = models.DecimalField(default=0.00, max_digits=65, decimal_places=2)
	seller = models.CharField(max_length=15)
	

	def __str__(self):
		return self.title


