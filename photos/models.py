from django.db import models

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length =40)
    
class Category(models.Model):
    category = models.CharField(max_length =40) 
    
class Images(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length =30)
    description = models.CharField(max_length =100)
    location = models.ForeignKey(Location,null = True)
    category = models.ForeignKey(Category, null = True)
    
    def __str__(self):
        return self.name
    
    def save_image(self):
        self.save()
        
   