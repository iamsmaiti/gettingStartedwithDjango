from django.urls import path
from . import views


urlpatterns = [
    path('', views.orderOverview, name="product-overview"),
    path('orderproduct-list/', views.orderproductlist, name="orderproduct-list"),
    path('orderproduct-detail/<int:pk>/', views.orderproductDetail, name="orderproduct-detail"),
    path('orderproduct-create/', views.orderproductCreate, name="orderproduct-create"),
    path('orderproduct-update/<int:pk>/', views.orderproductUpdate, name="orderproduct-update"),
    path('orderproduct-delete/<int:pk>/', views.orderproductDelete, name="orderproduct-delete"),
    
]