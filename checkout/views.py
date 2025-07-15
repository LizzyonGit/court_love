from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.conf import settings
from django.contrib import messages

from .forms import OrderForm

import stripe


@require_POST
def cache_checkout_data(request):
    """before we call the confirm card payment method in the stripe javascript, we make a post request
    to this view and give it the client secret from the payment intent, split it at the word secret to get the id
    then add metadata to it to get the save info by the user
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            #'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    
    except Exception as e:
        messages.error(request, 'Your payment could not be processed, try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty")
        return redirect(reverse('lessons'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
