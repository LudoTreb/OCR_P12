import logging

from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from event.models import Event
from event.permissions import EventPermission
from event.serializers import EventSerializer

logger = logging.getLogger('django')


class EventViewSet(ModelViewSet):
    """
    API endpoints to create, view, edit or delete an event
    """

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated, EventPermission]
