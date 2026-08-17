from rest_framework import permissions, viewsets
from .models import Topic, Post
from .serializers import TopicSerializer, PostSerializer

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.order_by("id")
    serializer_class = TopicSerializer
    permission_classes = [permissions.AllowAny]

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.order_by("id")
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]