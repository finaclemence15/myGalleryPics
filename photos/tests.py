from django.test import TestCase
from .models import Images,Location,Category

# Create your tests here.

class ImagesTestClass(TestCase):
        # Set up method
    def setUp(self):
        self.book= Images(image = 'book.jpg', name ='book', description ='about book')
        self.book1= Images(image = 'book1.jpg', name ='book1', description ='about book1')
        # self.book.save_images()

        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.book,Images))
        
        # Testing Save Method
    def test_save_method(self):
        self.book.save_image()
        images = Images.objects.all()
        self.assertTrue(len(images) > 0)
        
    def test_delete(self):
        self.book.save_image()
        self.book1.save_image()
        image = Images.objects.filter(image = 'book1.jpg').first()
        delete = Images.objects.filter(id = image.id).delete()
        images = Images.objects.all()
        self.assertTrue(len(images) == 1)

    def test_update(self):
        self.book.save_image()
        image = Images.objects.filter(image='book.jpg').first()
        update = Images.objects.filter(id = image.id).update(image='book1.jpg')
        updated= Images.objects.filter(image='book1.jpg').first()
        self.assertNotEqual(image.image,updated.image) 

    # def test_get_image_by_id(self):
    #     test_id = '1'
    #     id = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
    #     news_by_date = Article.days_news(date)
    #     self.assertTrue(len(news_by_date) == 0)  
    
class LocationTestClass(TestCase):
    
    def setUp(self):
        self.kigali= Location(location = 'Rwanda')
    
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kigali,Location))
        
    def test_save_method(self):
        self.kigali.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0) 
                           