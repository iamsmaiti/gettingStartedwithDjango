from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register('audit', views.DetailedAccountViewSet, basename='audit')
router.register('account', views.AccountViewSet, basename='account')
router.register('cart', views.CartViewSet, basename='cart')
router.register('addresses', views.AddressViewSet, basename='address')
router.register('items', views.ItemViewSet, basename='items')
router.register('orders', views.OrderViewSet, basename='orders')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    #path('api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token')
]

    
