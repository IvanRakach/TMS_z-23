from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Category


class CustomMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20


admin.site.register(Category, CustomMPTTModelAdmin)
