from django.shortcuts import (render, redirect, reverse, get_object_or_404,
                              HttpResponse)
from django.views.decorators.http import require_POST
from django.conf import settings
from django.contrib import messages

from .forms import OrderForm
from cart.contexts import cart_contents

from lessons.models import Lesson
from .models import OrderLineItem, Order
from profiles.forms import UserProfileForm
from profiles.models import UserProfile

from django.utils import timezone

import stripe
import json


@require_POST
def cache_checkout_data(request):
    """
    Handles save phone nr checkbox
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment can not be \
            processed right now. Try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    Handles payment completion
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone': request.POST['phone'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()
            for item_id, quantity in cart.items():
                try:
                    lesson = Lesson.objects.get(id=item_id)

                    order_line_item = OrderLineItem(
                        order=order,
                        lesson=lesson,
                        quantity=quantity,
                    )

                    # capacity handler
                    lesson.places_left -= order_line_item.quantity

                    lesson.save()

                    order_line_item.save()

                except Lesson.DoesNotExist:
                    messages.error(request, (
                        "One of the lessons in your cart was not found"
                        " in our database. "
                        " Call us for assistance.")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Double check your information.')

    else:

        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "Your cart is empty")
            return redirect(reverse('lessons'))

        # in case user passes cart view, when a lesson has no place left,
        # has been deleted or passed date, it should
        # go back to updated cart,
        # there you get the message about removed lesson
        for item_id in list(cart):
            lesson = Lesson.objects.get(id=item_id)

            if (lesson.places_left == 0
               or lesson.deleted or lesson.date_time < timezone.now()):
                return redirect(reverse('view_cart'))

        current_cart = cart_contents(request)

        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone': profile.default_phone,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing. \
                Did you forget to set it in your environment?')

        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handles successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone': order.phone,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed. \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
