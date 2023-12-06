from urllib import response
from django.test import TestCase
from django.urls import reverse
import books

from books.models import Category, Book

# Create your tests here.
# Model tests
class TestCategory(TestCase):
    """Test Category model"""

    def setUp(self):
        self.category = Category.objects.create(
            name="test cat",
            friendly_name="Test Cat"
        )
    
    def test_instance(self):
        """Test the category instance has been created"""
        self.assertEqual(self.category.name, "test cat")

    def test_str(self):
        """Test string method for Category"""
        self.assertEqual(str(self.category), "test cat")

    def test_get_friendly_name(self):
        """Test get friendly name method"""
        cat = Category.objects.get(name='test cat')
        friendly_name = cat.get_friendly_name()
        self.assertEqual(friendly_name, "Test Cat")


class TestBook(TestCase):
    """Test Book model"""

    def setUp(self):
        self.book = Book.objects.create(
            title="Test Title",
            summary="This is a test summary",
            author="Test author",
            isbn=123456789,
            price=5.99
        )
    
    def test_instance(self):
        """Test the book instance has been created with minimum data"""
        self.assertEqual(self.book.title, "Test Title")
    
    def test_str(self):
        """Test string method for Book"""
        self.assertEqual(str(self.book), "Test Title")


# Views tests
class TestBooksView(TestCase):
    """Testing the books view"""

    def test_url(self):
        """Test if the URL, response and template used"""
        response = self.client.get("/books/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "books/books.html")

    def test_url_name(self):
        """Test if the books url name is accessible by name"""
        response = self.client.get(reverse("books"))
        self.assertEqual(response.status_code, 200)
        

class TestBookSummaryView(TestCase):
    """Testing the book summary view"""

    def setUp(self):
        self.book = Book.objects.create(
            id=0,
            title="Test Book",
            summary="This is a test summary",
            author="Test Author",
            isbn=123456789,
            price=14.99
            )

    def test_url(self):
        """Test if the URL, response and template used"""
        response = self.client.get(f"/books/{self.book.id}")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "books/book_summary.html")