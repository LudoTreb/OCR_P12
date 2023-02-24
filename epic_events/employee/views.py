# Create your views here.

from django.contrib.auth.models import Group
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .models import User
from .permissions import EmployeePermission
from .serializers import UserSerializer, GroupSerializer


# Create your views here.
class UserViewSet(ModelViewSet):
    """
    API endpoints to create, view, edit or delete a User
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, EmployeePermission]


class GroupViewSet(ModelViewSet):
    """
    API endpoints to view, edit or delete a Group
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated, EmployeePermission]
