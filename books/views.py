from unicodedata import category
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Book, Category

# Create your views here.
def all_books(request):
    """This view displays all books, allows filtering by book categories and takes search queries"""

    books = Book.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(",")
            books = books.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)


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
        "query": query,
        "current_categories": categories
    }
    return render(request, "books/books.html", context)


def book_summary(request, book_id):
    """This view displays an individual summary of a selected book"""

    book = get_object_or_404(Book, id=book_id)

    context = {
        "book": book,
    }
    return render(request, "books/book_summary.html", context)
