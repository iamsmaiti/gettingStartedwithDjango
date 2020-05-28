from django.shortcuts import render
from user.models import User
from product.models import Item
from product.serializers import ItemSerializer

from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .serializers import AccountSerializer, AddressSerializer, CartSerializer, OrderSerializer, AuditSerializer
from .models import Address, Cart, Order


# Create your views here.
class AccountViewSet(viewsets.ModelViewSet):
    model = User
    serializer_class = AccountSerializer
    permission_classes = ()

    def post_save(self, obj, created=False):
        if created:
            cart = Cart(user=obj)
            cart.save()

    def get_queryset(self,):
        user = self.request.user
        return User.objects.filter(username=user.username)



class AddressViewSet(viewsets.ModelViewSet):
    model = Address
    serializer_class = AddressSerializer

    def get_queryset(self,):
        user = self.request.user
        return Address.objects.filter(user=user)

    def pre_save(self, obj):
        obj.user = self.request.user

class CartViewSet(viewsets.ModelViewSet):
    model = Cart
    serializer_class = CartSerializer

    def get_queryset(self,):
        return Cart.objects.filter(user=self.request.user)

    @action(methods=['post'], detail=True)
    def add(self, request, pk):
    	items = Item.objects.all()
    	serializer = ItemSerializer(items, many=True)
    	return Response({"success":True})
		

    def pre_save(self, obj):
        obj.user = self.request.user

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class OrderViewSet(viewsets.ModelViewSet):
    model = Order
    serializer_class = OrderSerializer
    def get_queryset(self,):
        return Order.objects.filter(user=self.request.user)

    def pre_save(self, obj):
        obj.user = self.request.user


class DetailedAccountViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = AuditSerializer
	permission_classes = (IsAdminUser)


