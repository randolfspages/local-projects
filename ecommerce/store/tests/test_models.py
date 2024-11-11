from django.test import TestCase
from django.contrib.auth.models import User

from store.models import Category, Product

# Create your tests here.

class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name="Pupil's Book 1", slug="pupil's-book-1")
    
def test_category_model_entry(self):
    # Test Category model data insertion/types/Field attributes
    data = self.data1
    self.assertTrue(isinstance(data, Category))
    
    
def test_category_model_entry(self):
    # Test Category model model default name
    data = self.data1
    self.assertEqual(str(data), "Pupil's Book 1")
    
    
    
class TestProductsModel(TestCase):
    def setUp(self):
        Category.objects.create(name="Pupil's Book 1", slug="pupil's-book-1")
        User.objects.create(username='range')
        self.data1 = Product.objects.create(category_id=1, title='Essential Science Primary 1', category_by_id=1, 
                                            slug='essential-science-primary-1', price=50, image='images/science_essentials.jpeg')
        
    
    def test_product_model_entry(self):
        # Test product model data insertion/types/field attributes
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'Essential Science Primary 1')