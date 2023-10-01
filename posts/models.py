from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    counter = models.PositiveIntegerField(default=0)