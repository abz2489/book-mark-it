from decimal import Decimal
from django.conf import settings


def basket_contents(request):

    basket_items = []
    total_price = 0
    items = 0

    delivery = total_price * Decimal(settings.DELIVERY_PECENTAGE / 100)

    grand_total = total_price + delivery
    context = {
        "basket_items": basket_items,
        "total_price": total_price,
        "items": items,
        "delivery": delivery,
        "grand_total": grand_total
    }
    return context