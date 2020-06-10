from user.models import User
from rest_framework import serializers

from .models import Address, Cart, Order


class AccountSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model= User
		fields= ('username', 'email', 'password', 'address', 'carts')
		write_only_fields= ('password')

	def restore_object(self, attrs, instance=None):
		user = super(AccountSerializer, self).restore_object(attrs, instance)
		user.set_password(attrs['password'])
		return user

class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ( 'first_name','last_name','street_address1','street_address2', 'city', 'state', 'phone', 'url')

class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ( 'items')

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ( 'url', 'items','cart')

class AuditSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'password', 'addresses','carts')
        write_only_fields = ('password',)
        depth = 3
		









       