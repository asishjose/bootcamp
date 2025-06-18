from django.db import models

# Create your models here.
class FamilyMember(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    housename = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)


    def __str__(self):
        return self.name