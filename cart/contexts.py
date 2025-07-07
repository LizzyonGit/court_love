from decimal import Decimal
from django.conf import settings

def cart_contents(request):

    cart_items = []
    product_count = 0
    grand_total = 0

    context = {
        'cart_items': cart_items,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context
