from django.contrib import admin
from django.db.models import Sum
from django.db.models import Count

from phone_orders.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'pk', 'user', 'status'
    ]
    readonly_fields = ['total_price', 'number_of_goods']

    def total_price(self, obj):
        print(f'set - {obj.items.all()}')
        total = obj.items.aggregate(Sum('price')).values()
        # print(f'total - {type(total)}')
        return f'{list(total)[0]} BYN'

    def number_of_goods(self, obj):
        total = obj.items.aggregate(total_number_of_products_in_order=Count('price')).values()
        return f'{list(total)[0]}'


admin.site.register(Order, OrderAdmin)
