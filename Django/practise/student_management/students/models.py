from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField(null=True)
    address = models.TextField()

    def __str__(self):
        return self.name