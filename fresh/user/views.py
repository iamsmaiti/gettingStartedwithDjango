from rest_framework import permissions, viewsets
from rest_framework.exceptions import PermissionDenied
from .models import User
from .serializers import UserSerializer

class IsUser(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		return obj.user == request.user

class UserViewSet(viewsets.ModelViewSet):
	serializer_class = UserSerializer
	permission_classes = (IsUser,)

	def get_queryset(self):
		user = self.request.user
		if user.is_authenticated:
			return User.object.filter(user=user)
		raise PermissionDenied()

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)








    

