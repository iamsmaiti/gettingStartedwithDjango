from rest_framework import serializers
from .models import Item

#serializing all fields
class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = '__all__'