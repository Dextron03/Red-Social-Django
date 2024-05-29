from django.db import models
from post.models import Posts
from MysocialUser.models import MySocialUser

# Create your models here.
class Comment(models.Model):
    content = models.TextField(max_length=200)
    posts = models.ForeignKey(to=Posts, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(to=MySocialUser, related_name="comments", on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.user} | {self.posts.pk}"
