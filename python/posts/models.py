from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    id = models.AutoField(primary_key=True) 
    user = models.name = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=False)
    updated_at = models.DateTimeField(auto_now_add=False)

class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = [['post_id', 'user_id']]