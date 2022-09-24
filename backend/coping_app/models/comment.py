from django.db import models
from .post import Post
from .user import CustomUser

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, models.SET_NULL, blank=True, null=True)
    content = models.CharField(max_length=1000)