from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=255)
    username = models.CharField(max_length=100)
    passhash = models.CharField(max_length=255)
    register_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anime_id = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.email} on Anime {self.anime_id}"