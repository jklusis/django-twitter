from django.db import models
from django.contrib.auth.models import User

class UserFollow(models.Model):
    id = models.AutoField(primary_key=True) 
    following_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_that_is_following')
    followed_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_that_is_being_followed')
    created_at = models.DateTimeField(auto_now_add=True)