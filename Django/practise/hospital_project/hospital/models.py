from django.db import models

# Create your models here.
class Doctor(models.Model):
    name=models.CharField(max_length=100)
    specialization=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Patient(models.Model):
    name=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    def __str__(self):
        return self.name