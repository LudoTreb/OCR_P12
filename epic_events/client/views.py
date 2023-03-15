import logging

from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from client.models import Client, Contract
from client.permissions import ClientPermission, ContractPermission
from client.serializers import ClientSerializer, ContractSerializer

logger = logging.getLogger('django')


class ClientViewSet(ModelViewSet):
    """
    API endpoints to create, view or edit a client
    """

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated, ClientPermission]


class ContractViewSet(ModelViewSet):
    """
    API endpoints to create, view or edit a contract
    """

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [permissions.IsAuthenticated, ContractPermission]


class SelfContractViewset(ModelViewSet):
    serializer_class = ContractSerializer

    def get_queryset(self):
        queryset = Contract.objects.all()
        contract_signed = self.request.query_params.get('is_signed')
        contract_amount = self.request.query_params.get('amount')

        if contract_amount is not None:
            queryset = queryset.filter(amount=contract_amount)

        if contract_signed is not None:
            queryset = queryset.filter(is_signed=contract_signed)

        return queryset
