from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages

from books.models import Book

# Create your views here.
def view_basket(request):
    """A view that renders basket items page"""

    return render(request, "basket/basket.html")


def add_to_basket(request, book_id):
    """Add book quantity to basket"""

    book = get_object_or_404(Book, id=book_id)
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    basket = request.session.get('basket', {})

    if book_id in list(basket.keys()):
        basket[book_id] += quantity
        messages.success(request, f'Updated {book.title} quantity to {basket[book_id]}')
    else:
        basket[book_id] = quantity
        messages.success(request, f'Added {book.title} by {book.author} to your basket')

    request.session["basket"] = basket
    return redirect(redirect_url)


def adjust_basket(request, book_id):
    """Adjust quantity of books in basket"""
    
    book = get_object_or_404(Book, id=book_id)
    quantity = int(request.POST.get("quantity"))
    basket = request.session.get("basket", {})

    if quantity > 0:
            basket[book_id] = quantity
            messages.success(request, f'Updated {book.title} quantity to {basket[book_id]}')
    else:
            basket.pop(book_id)
            messages.success(request, f'Removed {book.title} quantity to {basket[book_id]}')

    request.session["basket"] = basket
    return redirect(reverse("basket"))

def remove_from_basket(request, book_id):
    """Remove a selected book from the basket"""

    book = get_object_or_404(Book, id=book_id)

    try:
        basket = request.session.get("basket", {})
        basket.pop(book_id)
        messages.success(request, f'Removed {book.title} from your basket')
        request.session["basket"] = basket

        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)