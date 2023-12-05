from django.test import TestCase
from django.db import IntegrityError

from books.models import Category

# Models tests
class TestCategoryModel(TestCase):
    CAT_NAME = "test cat"
    CAT_FRIENDLY_NAME = "Test Cat"

    def setUp(self):
        self.category = Category.objects.create(
            name=self.CAT_NAME,
            friendly_name=self.CAT_FRIENDLY_NAME
        )

    def test_instance(self):
        """Test category can be created with just the name field"""
        self.assertEqual(self.category.name, self.CAT_NAME)

    def test_str(self):
        """Test the string method"""
        self.assertEqual(self.CAT_NAME, str(self.category))

    def test_get_friendly_name(self):
        """Test get friendly name method"""
        saved_category = Category.objects.get(name=self.CAT_NAME)
        f_name_return = saved_category.get_friendly_name()
        self.assertEqual(f_name_return, self.CAT_FRIENDLY_NAME)
    