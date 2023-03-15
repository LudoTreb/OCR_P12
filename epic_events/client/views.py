import logging

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from client.models import Client, Contract
from client.permissions import ClientPermission, ContractPermission
from client.serializers import ClientSerializer, ContractSerializer

logger = logging.getLogger("django")


class ClientViewSet(ModelViewSet):
    """
    API endpoints to create, view or edit a client
    """

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated, ClientPermission]
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
    ]
    search_field = ["last_name", "email"]
    filterset_fields = ["last_name", "email"]


class ContractViewSet(ModelViewSet):
    """
    API endpoints to create, view or edit a contract
    """

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [permissions.IsAuthenticated, ContractPermission]
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
    ]
    search_field = ["client__last_name", "client__email", "=amount", "=date_created"]
    filterset_fields = [
        "is_signed",
        "amount",
    ]
