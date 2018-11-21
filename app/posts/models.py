from django.db import models

from config import settings


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='작성자',
    )
    photo = models.ImageField(
        '사진',
        upload_to='post',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    content = models.TextField()
    tags = models.ManyToManyField(
        'HashTag',
        blank=True,
    )


class HashTag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


