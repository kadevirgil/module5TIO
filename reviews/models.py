from django.db import models

# Create your models here.
class Review(models.Model): 
    username = models.CharField(max_length=100)
    email = models.EmailField()
    feedback = models.TextField()