from django.db import models
from django.urls import reverse
from datetime import datetime

class Subscribe(models.Model):
    email = models.EmailField()

class Post(models.Model):
    title = models.CharField(max_length= 150)
    body = models.TextField()
    date = models.DateTimeField()
    author= models.TextField(default='Sunny awugo')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

    class Meta:
        ordering = ["-date"]

class Comment(models.Model):
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


class AudioMessages(models.Model):
    title = models.CharField(max_length= 30)
    link = models.URLField(max_length=200)

class Letter(models.Model):
    subEmail = models.EmailField()
