from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Displays order line items in the order.
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    Specifies fields, readonly fields, which fields are in list dispaly,
    which field can be searched, order to display orders
    """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'order_date',
                       'grand_total', 'original_cart', 'stripe_pid',)

    fields = ('order_number', 'user_profile', 'order_date', 'full_name',
              'email', 'phone', 'grand_total', 'original_cart', 'stripe_pid',)

    list_display = ('order_number', 'order_date', 'user_profile',
                    'user_profile__level',)
    search_fields = ('order_number',)

    ordering = ('-order_date',)


@admin.register(OrderLineItem)
class OrderLineItemAdmin(admin.ModelAdmin):
    """
    Specifies which fields are in list dispalay,
    and which can be filtered.
    """
    list_display = ('order', 'lesson', 'lesson__date_time',
                    'lesson__level_interval',
                    'order__user_profile', 'order__user_profile__level',)

    list_filter = ('lesson__date_time',)


admin.site.register(Order, OrderAdmin)
