from rest_framework import permissions, viewsets
from .models import Topic, Post
from .serializers import TopicSerializer, PostSerializer
from rest_framework import generics

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.order_by("id")
    serializer_class = TopicSerializer
    permission_classes = [permissions.AllowAny]

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.order_by("id")
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]

class ListPostsOfTopic(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        topicID = self.kwargs.get("topicID")
        data = Post.objects.filter(topic = topicID)
        return data