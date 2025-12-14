from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    def get_absolute_url(self):
        return reverse(
            "blog:post-detail",
            kwargs={"pk": self.pk}
        )

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"Comment by {self.author.username} on {self.post.title}"
        )
