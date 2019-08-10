from django.db import models

# Create your models here.


class Property(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.TextField()
