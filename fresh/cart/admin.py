from django.contrib import admin
from .models import Cart, Address, Order

admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Address)

# Register your models here.
