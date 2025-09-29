from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class User(models.Model):
    username = models.CharField(verbose_name='Никнейм', max_length=30)
    email = models.EmailField("E-mail", unique=True)
    avatar = models.URLField(default="https://simpsonsforyou.ru/wp-content/uploads/2019/05/S6222_.png")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    
class Genre(models.Model):
    name = models.CharField("Название жанра", max_length=100)
    def __str__(self):
        return self.name
    
class Game(models.Model):
    name = models.CharField("Название игры", max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    release_date = models.DateField()
    trailer_url = models.URLField(null=True, blank=True)
    preview_url = models.URLField(null=True, blank=True)
    def __str__(self):
        return self.name
    
class GameGenre(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

class Library(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    purchased_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Library"
        verbose_name_plural = "libraries"


class Friendship(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Друг1")
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Друг2")
    status = models.CharField(max_length=50)

class Balance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.CharField(max_length=200)

class Media(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    type_media = models.CharField(max_length=50)
    link = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = "Media"
        verbose_name_plural = "Media"

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    desciption = models.TextField()
    amount_likes = models.PositiveIntegerField(default=0)
    media_URL= models.URLField(null=True, blank=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    amount_likes = models.PositiveIntegerField(default=0)
    
class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1),  MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)

class ReviewComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


    
