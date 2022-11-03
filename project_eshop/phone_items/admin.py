from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from phone_items.models import Brand, Product, Item

admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Item)
