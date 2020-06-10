from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import UserViewSet

router = SimpleRouter()
router.register('user', UserViewSet, basename="user")


#urlpatterns += router.urls

urlpatterns = router.urls