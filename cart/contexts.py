from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from lessons.models import Lesson


def cart_contents(request):
    """Handles adding lesson to cart"""

    cart_items = []
    product_count = 0
    grand_total = 0

    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        lesson = get_object_or_404(Lesson, pk=item_id)
        grand_total += quantity * lesson.price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'lesson': lesson,
        })

    context = {
        'cart_items': cart_items,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context
