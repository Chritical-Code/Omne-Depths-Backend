from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=30)

class Post(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    text = models.TextField()