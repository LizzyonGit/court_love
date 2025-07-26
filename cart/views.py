from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from lessons.models import Lesson

# Create your views here.


def view_cart(request):
    """Returns cart contents page"""
    cart = request.session.get('cart', {})
    print(cart)
    print(cart.items())

    # if places_left is 0, should remove from cart and give message
    # https://www.geeksforgeeks.org/python/python-delete-items-from-dictionary-while-iterating/
    for item_id in list(cart):
        lesson = Lesson.objects.get(id=item_id)
        try:
            if lesson.places_left == 0:
                del cart[item_id]
                messages.error(request, 'One or more lessons in your cart did not have places left. They have been removed.')
        except:
            pass

    print(cart)

    # update cart so chekout gets correct cart
    request.session['cart'] = cart


    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """Add lesson to cart"""
    # get lessons for message
    lesson = get_object_or_404(Lesson, pk=item_id)

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
    lesson = get_object_or_404(Lesson, pk=item_id)

    redirect_url = request.POST.get('redirect_url')

    try:
        cart = request.session.get('cart', {})
        cart.pop(item_id)
        messages.success(request, f'Removed {lesson.name} from cart')

        request.session['cart'] = cart

        return redirect(redirect_url)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return redirect(redirect_url)
