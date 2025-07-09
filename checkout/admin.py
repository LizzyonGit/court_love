from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'order_date',
                       'grand_total',)

    fields = ('order_number', 'order_date', 'full_name',
              'email', 'phone', 'grand_total',)

    list_display = ('order_number', 'order_date', 'full_name',)

    ordering = ('-order_date',)


admin.site.register(Order, OrderAdmin)
