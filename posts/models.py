from django.db import models

class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        """String rep of the model"""
        return self.text[:50] 
