from rest_framework import permissions, viewsets
from .models import Topic
from .serializers import TopicSerialzer

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.order_by('?')[:33]
    serializer_class = TopicSerialzer
    permission_classes = [permissions.AllowAny]