from django.db import models
from MysocialUser.models import MySocialUser

class Friends(models.Model):
    user = models.ForeignKey(to=MySocialUser, related_name='friends', on_delete=models.CASCADE, default=None)  
    friend = models.ForeignKey(to=MySocialUser, related_name='friends_of', on_delete=models.CASCADE, default=None)  
    stablished_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['user', 'friend'] 

    def __str__(self) -> str:
        return f'{self.friend.username}' 

