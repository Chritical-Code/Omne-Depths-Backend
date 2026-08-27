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
        topicName = self.kwargs.get("topicName")
        posts = Post.objects.filter(topic__name__iexact = topicName)
        return posts

class GenerateTopics(generics.ListAPIView):
    serializer_class = TopicSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        # generate new topics

        # send new topics generated
        
        topics = Topic.objects.all()
        return topics