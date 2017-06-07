from django.db import models
from utils.models.mixins import TimeStampedMixin


class Post(TimeStampedMixin):
    author = models.ForeignKey('User')
    title = models.CharField(max_length=50)
    content = models.TextField()


class Comment(TimeStampedMixin):
    post = models.ForeignKey(Post)
    author = models.ForeignKey('User')
    content = models.TextField()


class User(TimeStampedMixin):
    name = models.CharField(max_length=10)
