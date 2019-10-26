from django.test import TestCase
from .models import Images,Location,Category

# Create your tests here.

class ImagesTestClass(TestCase):
        # Set up method
    def setUp(self):
        self.book= Images(image = 'book.jpg', name ='book', description ='about book')
        self.book1= Images(image = 'book1.jpg', name ='book1', description ='about book1')

        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.book,Images))
        
        # Testing Save Method of Image model
    def test_save_method(self):
        self.book.save_image()
        images = Images.objects.all()
        self.assertTrue(len(images) > 0)
        
    # Testing  delete method of Image model    
    def test_delete(self):
        self.book.save_image()
        self.book1.save_image()
        image = Images.objects.filter(image = 'book1.jpg').first()
        delete = Images.objects.filter(id = image.id).delete()
        images = Images.objects.all()
        self.assertTrue(len(images) == 1)

    # Testing  update method of Image model
    def test_update(self):
        self.book.save_image()
        image = Images.objects.filter(image='book.jpg').first()
        update = Images.objects.filter(id = image.id).update(image='book1.jpg')
        updated= Images.objects.filter(image='book1.jpg').first()
        self.assertNotEqual(image.image,updated.image) 
    
class LocationTestClass(TestCase):
    
    # set Up method
    def setUp(self):
        self.kigali= Location(location = 'Rwanda')
    
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kigali,Location))
    
    # Testing  save method of Location model    
    def test_save_method(self):
        self.kigali.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)
    
    # Testing  delete method of Location model    
    def test_delete(self):
        self.kigali.save_location()
        location = Location.objects.filter(location = 'Rwanda').first()
        delete = Location.objects.filter(id = location.id).delete()
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)
    
    
    # Testing  update method of Location model    
    def test_update(self):
        self.kigali.save_location()
        location = Location.objects.filter(location = 'Rwanda').first()
        update = Location.objects.filter(id = location.id).update(location = 'Nyarugenge')
        updated = Location.objects.filter(location = 'Nyarugenge').first()
        self.assertNotEqual(location.location, updated.location)
        
class CategoryTestClass(TestCase):
    def setUp(self):
        self.travel = Category(category = 'food')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.travel,Category))   
        
    # Testing  save method of Category model
    def test_save_method(self):
        self.travel.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)
        
    # Testing  delete method of Category model  
    def test_delete(self):
        self.travel.save_category()
        category = Category.objects.filter(category = 'food').first()
        delete = Category.objects.filter(id = category.id).delete()
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 0)  
        
                  
    # Testing  Update method of Category model
    
    def test_update(self):
        self.travel.save_category()
        category = Category.objects.filter(category = 'food').first()
        update = Category.objects.filter(id = category.id).update(category = 'cars')
        updated = Category.objects.filter(category = 'cars').first()
        self.assertNotEqual(category.category, updated.category)             
                           