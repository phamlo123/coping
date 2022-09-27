from django.db import models
from .post import Post
from .user import CustomUser

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', related_name="comments", on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)