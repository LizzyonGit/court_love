from django.shortcuts import render, redirect
from django.contrib import messages
from lessons.models import Lesson

# Create your views here.


def view_cart(request):
    """Returns cart contents page"""
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """Add lesson to cart"""
    # get lessons for message
    lesson = Lesson.objects.get(pk=item_id)

    quantity = int(request.POST.get('quantity'))

    redirect_url = request.POST.get('redirect_url')

    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        # should I prevent adding item to cart?
        cart[item_id] += quantity
        messages.success(request, f'Added {lesson.name} to cart')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {lesson.name} to cart')

    request.session['cart'] = cart

    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """Remove item from cart"""
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    cart.pop(item_id)

    request.session['cart'] = cart

    return redirect(redirect_url)
