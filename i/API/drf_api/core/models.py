from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self) -> str:
        return self.title