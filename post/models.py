from django.db import models
from MysocialUser.models import MySocialUser

# Create your models here.
class Posts(models.Model):
    content_posts = models.TextField(max_length=400, verbose_name='Contenido')
    img = models.ImageField(upload_to='img_posts/', blank=True, null=True)
    hour = models.DateTimeField(auto_now_add=True)  
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(to=MySocialUser, related_name='posts', on_delete=models.CASCADE) 
    
    def __str__(self) -> str:
        return f"{self.user} | {self.content_posts}"