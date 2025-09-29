from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(verbose_name='Никнейм', max_length=30)
    email = models.EmailField("E-mail", unique=True)
    avatar = models.ImageField("Аватарка", upload_to='avatars', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    
class Genre(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name