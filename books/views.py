from unicodedata import category
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Book

# Create your views here.
def all_books(request):
    """This view displays all books"""

    books = Book.objects.all()
    query = None

    if request.GET:
        if "q" in request.GET:
            query = request.GET["q"]
            print(f"Query: {query}")
            if not query:
                messages.error(request, "No search criteria entered!")
                return redirect(reverse('books'))

            queries = Q(title__icontains=query) | Q(category__name__icontains=query) | Q(author__icontains=query)
            books = books.filter(queries)

    context = {
        "books": books,
        "search_term": query
    }
    return render(request, "books/books.html", context)


def book_summary(request, book_id):
    """This view displays an individual summary of a selected book"""

    books = get_object_or_404(Book, id=book_id)

    context = {
        "books": books,
    }
    return render(request, "books/book_summary.html", context)
