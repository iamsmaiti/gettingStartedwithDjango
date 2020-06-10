from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StoreSerializer
from .models import Store

# Create your views here.

@api_view(['GET'])
def storeOverview(request):
	store_urls = {
		'List':'/store-list/',
		'Detail View':'/store-detail/<int:pk>/',
		'Create':'/store-create/',
		'Update':'/store-update/<int:pk>',
		'Delete':'/store-delete/<int:pk>/',
		}
	return Response(product_urls)


@api_view(['GET'])
def storelist(request):
	stores = Store.objects.all()
	serializer = StoreSerializer(stores, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def storeDetail(request, pk):
	stores = Store.objects.get(id=pk)
	serializer = StoreSerializer(stores, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def storeCreate(request):
	serializer = StoreSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['POST'])
def storeUpdate(request, pk):
	store = Store.objects.get(id=pk)
	serializer = StoreSerializer(instance=store, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['DELETE'])
def storeDelete(request, pk):
	store = Store.objects.get(id=pk)
	store.delete()
	return Response("There's nothing! It's deleted")




