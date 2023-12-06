from django.test import TestCase

from books.models import Category, Book

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

    def test_str(self):
        """Test string method for Category"""
        self.assertEqual(str(self.category), self.CAT_NAME)

    def test_get_friendly_name(self):
        """Test get friendly name method"""
        cat = Category.objects.get(name=self.CAT_NAME)
        friendly_name = cat.get_friendly_name()
        self.assertEqual(friendly_name, self.CAT_FRIENDLY_NAME)


class TestBook(TestCase):
    BOOK_TITLE = "Test Title"
    BOOK_SUMMARY = "This is a test summary for {BOOK_TITLE}"
    BOOK_AUTHOR = "Test author"
    BOOK_ISBN = 123456789
    BOOK_PRICE = 5.99

    def setUp(self):
        self.book = Book.objects.create(
            title=self.BOOK_TITLE,
            summary=self.BOOK_SUMMARY,
            author=self.BOOK_AUTHOR,
            isbn=self.BOOK_ISBN,
            price=self.BOOK_PRICE
        )
    
    def test_instance(self):
        """Test the book instance has been created with minimum data"""
        self.assertEqual(self.book.title, self.BOOK_TITLE)
    
    def test_str(self):
        """Test string method for Book"""
        self.assertEqual(str(self.book), self.BOOK_TITLE)