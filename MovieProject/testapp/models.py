from django.db import models

from django.db import models
class Movie(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    hero=models.CharField(max_length=10)
    heroine=models.CharField(max_length=10)
