from rest_framework import serializers
from .models import Topic


class TopicSerialzer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topic
        fields = ["topic"]