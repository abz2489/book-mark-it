from django.shortcuts import get_object_or_404, render
from .models import Book

# Create your views here.
def all_books(request):
    """This view displays all books"""

    books = Book.objects.all()

    context = {
        "books": books,
    }
    return render(request, "books/books.html", context)


def book_summary(request, book_id):
    """This view displays an individual summary of a selected book"""

    book = get_object_or_404(Book, id=book_id)

    context = {
        "book": book,
    }
    return render(request, "books/book_summary.html", context)