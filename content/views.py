from rest_framework import permissions, viewsets
from .models import Topic, Post
from .serializers import TopicSerializer, PostSerializer
from rest_framework import generics
from .ai.topic_generator import TopicGenerator
import json
from .pagination import CustomPaginator
from django.db.models.functions import Random


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.order_by("id")                                         # in order
    # queryset = Topic.objects.annotate(random=Random()).order_by("random")[:100]   # random

    serializer_class = TopicSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = CustomPaginator

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
        topics = Topic.objects.order_by("id")[:100]

        # attach new topics to base prompt
        exclude = ""
        for topic in topics:
            exclude += topic.name + ", "

        # send prompt to ai
        ai = TopicGenerator(exclude=exclude)
        ai.real_ai_call()

        # convert ai response to json
        topics_dict = json.loads(ai.response)

        # check for error message
        if "error" in topics_dict:
            return

        # convert json to objects
        new_topics = list()
        for temp_topic in topics_dict:
            # check for duplicates
            skip = False
            for topic in topics:
                if temp_topic["name"] == topic.name:
                    skip = True

            # convert and save
            if not skip:
                new_topic = Topic(name=temp_topic["name"])
                new_topics.append(new_topic)
                new_topic.save()


        # return new topics generated
        return new_topics