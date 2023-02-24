
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from client.models import Client, Contract
from client.permissions import ClientPermission, ContractPermission
from client.serializers import ClientSerializer, ContractSerializer


class ClientViewSet(ModelViewSet):
    """
    API endpoints to create, view, edit or delete a client
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated, ClientPermission]


class ContractViewSet(ModelViewSet):
    """
    API endpoints to create, view, edit or delete a contract
    """
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [permissions.IsAuthenticated, ContractPermission]
