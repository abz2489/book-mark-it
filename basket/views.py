from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_basket(request):
    """A view that renders basket items page"""

    return render(request, "basket/basket.html")


def add_to_basket(request, book_id):
    """Add book quantity to basket"""
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    basket = request.session.get('basket', {})

    if book_id in list(basket.keys()):
        basket[book_id] += quantity
    else:
        basket[book_id] = quantity

    request.session["basket"] = basket
    return redirect(redirect_url)


def adjust_basket(request, book_id):
    """Adjust quantity of books in basket"""
    print("Adjusting quantity....")
    quantity = int(request.POST.get("quantity"))
    basket = request.session.get("basket", {})

    if quantity > 0:
            basket[book_id] = quantity
    else:
            basket.pop(book_id)

    request.session["basket"] = basket
    print(f"quantity = {quantity}")
    return redirect(reverse("basket"))