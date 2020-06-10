from django.urls import path
from . import views


urlpatterns = [
    path('', views.storeOverview, name="store-overview"),
    path('store-list/', views.storelist, name="store-list"),
    path('store-detail/<int:pk>/', views.storeDetail, name="store-detail"),
    path('store-create/', views.storeCreate, name="store-create"),
    path('store-update/<int:pk>/', views.storeUpdate, name="store-update"),
    path('store-delete/<int:pk>/', views.storeDelete, name="store-delete"),
    
]