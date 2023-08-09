from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=50)
    full_name=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    gender=models.CharField(max_length=10)

    def __str__(self):
        return self.username