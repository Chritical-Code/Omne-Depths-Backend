from rest_framework import permissions, viewsets
from .models import Topic, Post
from .serializers import TopicSerializer, PostSerializer
from rest_framework import generics
from .ai import TopicGenerator

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
        # gather all current topics
        topics = Topic.objects.order_by("id")

        # attach new topics to base prompt
        exclude = ""
        for topic in topics:
            exclude += topic.name + ", "

        # send prompt to ai
        ai = TopicGenerator(exclude=exclude)

        # print a basic test response
        ai.test_ai_call()

        # convert ai response to json or object or etc

        # create new topic object array with ai response
        newTopics = list()
        newTopic = Topic(name="")
        newTopics.append(newTopic)

        # remove any duplicates found

        # save topics to database

        # return new topics generated
        return topics