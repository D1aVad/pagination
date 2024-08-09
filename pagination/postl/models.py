from django.db import models
from django.utils.html import strip_tags

# Модель поста
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_time = models.DateTimeField()


    def __str__(self):
        return self.title
