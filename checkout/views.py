from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get("basket", {})
    print(basket)
    if not basket:
        messages.error(request, "Your basket is empty")
        return redirect(reverse("books"))

    order_form = OrderForm()
    template = "checkout/checkout.html"
    context = {
        "order_form": order_form,
        "stripe_public_key": "pk_test_51O6bBTGVFwjsxy1SVYm6dlQovw8v4wARXNc2xTsmTpYRoKn0V654SBChD3JNtwS1P2IqMpEUvxRNacsjaNEdK5h100thy01r6a",
        "client_secret": "test_client_secret"
    }

    return render(request, template, context)