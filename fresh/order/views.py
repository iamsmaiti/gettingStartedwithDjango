from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import OrderProductSerializer
from .models import OrderProduct
# Create your views here.


@api_view(['GET'])
def orderOverview(request):
	order_urls = {
		'List':'/orderproduct-list/',
		'Detail View':'/orderproduct-detail/<int:pk>/',
		'Create':'/orderproduct-create/',
		'Update':'/orderproduct-update/<int:pk>',
		'Delete':'/orderproduct-delete/<int:pk>/',
		}

	return Response(order_urls)

@api_view(['GET'])
def orderproductlist(request):
	orderproducts = OrderProduct.objects.all()
	serializer = OrderProductSerializer(orderproducts, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def orderproductDetail(request, pk):
	orderproduct = OrderProduct.objects.get(id=pk)
	serializer = OrderProductSerializer(orderproducts, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def orderproductCreate(request):
	serializer = OrderProductSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)


@api_view(['POST'])
def orderproductUpdate(request, pk):
	orderproduct = OrderProduct.objects.get(id=pk)
	serializer = OrderProductSerializer(instance=orderproduct, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)


@api_view(['DELETE'])
def orderproductDelete(request, pk):
	orderproduct = OrderProduct.objects.get(id=pk)
	orderproduct.delete()
	return Response("There's nothing! It's deleted")



