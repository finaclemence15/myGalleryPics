from django.db import models

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length =40)
    
    def __str__(self):
        return self.location
        
    def save_location(self):
        self.save()    
    
class Category(models.Model):
    category = models.CharField(max_length =40) 
    
    def __str__(self):
        return self.category
        
    def save_category(self):
        self.save()
            
class Images(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length =30)
    description = models.TextField()
    location = models.ForeignKey(Location,null = True)
    category = models.ForeignKey(Category, null = True)
    
    def __str__(self):
        return self.name
    
    @classmethod
    def search_by_category(cls,search_term):
        image = cls.objects.filter(category__category=search_term)
        return image    
    
    def save_image(self):
        self.save()
        
        #    

    @classmethod
    def filter_location(cls,location):
        filter_loc = cls.objects.filter(image__location__icontains=location)
        return filter_loc


    @classmethod
    def get_image_by_id(cls,input_id):
        image_got = cls.objects.get(id=input_id)
        return image_got        