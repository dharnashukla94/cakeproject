from django.db import models

# Create your models here.

class DataDescription(models.Model):
    name = models.CharField(max_length=20)
    desc = models.TextField()
    price = models.FloatField()
    img = models.ImageField(upload_to='pics')



