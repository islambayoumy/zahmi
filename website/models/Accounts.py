from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    
    user = models.OneToOneField(User)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "User Profile"
        ordering = ['-timestamp']

    def __str__(self):
        return self.user

        