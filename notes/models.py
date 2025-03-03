from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    noLikes = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
