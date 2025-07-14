import uuid

from django.conf import settings
from django.db import models
from core.models import TimeStampedModel
 
class Question(TimeStampedModel):
    content = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return self.content
    
class Answer(TimeStampedModel):
    body = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    voters = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='votes', blank=True)

    def __str__(self):
        return self.author.username