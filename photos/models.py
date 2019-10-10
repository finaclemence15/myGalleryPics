from django.db import models

# Create your models here.
class Images(models.Model):
    image = models.ImageField(upload_to = 'images/',null = True)
    name = models.CharField(max_length =30)
    description = models.CharField(max_length =100)
    location = models.CharField(max_length =30)
    category = models.CharField(max_length =30)
    
    