from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from books.models import Book


def basket_contents(request):
    basket_items = []
    total_price = 0
    items = 0
    basket = request.session.get("basket", {})

    for book_id, quantity in basket.items():
        book = get_object_or_404(Book, id=book_id)
        total_price += quantity * book.price
        items += quantity
        basket_items.append({
            "book_id": book_id,
            "quantity": quantity,
            "book": book,
            "total_price": total_price
        })

    if total_price < settings.FREE_DELIVERY:
        delivery = total_price * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    else:
        delivery = 0
    
    delivery = total_price * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)

    grand_total = total_price + delivery
    context = {
        "basket_items": basket_items,
        "total_price": total_price,
        "items": items,
        "delivery": delivery,
        "grand_total": grand_total
    }
    return context