from rest_framework import viewsets
from events.models import Event
from .serializers import EventSerializer

class EventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
