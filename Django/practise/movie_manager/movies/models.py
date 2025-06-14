from django.db import models

# Create your models here.
class MovieInfo(models.Model):
    title=models.CharField(max_length=100)
    year=models.IntegerField()
    description=models.TextField(default='No description')