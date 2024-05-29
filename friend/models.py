from django.db import models
from MysocialUser.models import MySocialUser

# Create your models here.
class Friends(models.Model):
    user = models.ForeignKey(MySocialUser, on_delete=models.CASCADE, related_name='user_friends')
    friend = models.ForeignKey(MySocialUser, on_delete=models.CASCADE, related_name='friend_of')
    stablished_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['user', 'friend'] 

    def __str__(self) -> str:
        return f'{self.friend.username}' 