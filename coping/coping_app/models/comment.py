from django.db import models
from .post import Post
from .user import User

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    content = models.CharField(max_length=1000)