from django.test import TestCase

from books.models import Category

# Create your tests here.
class TestCategory(TestCase):
    """Test Category model"""
    CAT_NAME = "test cat"
    CAT_FRIENDLY_NAME = "Test Cat"

    def setUp(self):
        self.category = Category.objects.create(
            name=self.CAT_NAME,
            friendly_name=self.CAT_FRIENDLY_NAME
        )
    
    def test_instance(self):
        """Test the category instance has been created"""
        self.assertEqual(self.category.name, self.CAT_NAME)
        self.assertEqual(self.category.friendly_name, self.CAT_FRIENDLY_NAME)

    def test_str(self):
        """Test string method"""
        self.assertEqual(str(self.category), self.CAT_NAME)

    def test_get_friendly_name(self):
        """Test get friendly name method"""
        cat = Category.objects.get(name=self.CAT_NAME)
        friendly_name = cat.get_friendly_name()
        self.assertEqual(friendly_name, self.CAT_FRIENDLY_NAME)