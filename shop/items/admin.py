from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Category, Product, Item


class CustomMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20


admin.site.register(Category, CustomMPTTModelAdmin)
admin.site.register(Product)
admin.site.register(Item)
