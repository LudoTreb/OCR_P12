import logging

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from event.models import Event
from event.permissions import EventPermission
from event.serializers import EventSerializer

logger = logging.getLogger("django")


class EventViewSet(ModelViewSet):
    """
    API endpoints to create, view, edit or delete an event
    """

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated, EventPermission]
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ["client__last_name", "client__email", "=date_created"]
    filterset_fields = ["event_status"]
