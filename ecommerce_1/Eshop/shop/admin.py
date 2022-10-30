from django.contrib import admin
from django.utils.safestring import mark_safe
from shop.models import *

admin.site.site_title = "My Marketplace"
admin.site.site_header = "My Marketplace"


class PhoneAdmin(admin.ModelAdmin):
    list_display = [
        'phone_brand', 'phone_model', 'phone_price', 'get_image',
        'phone_reserve', 'phone_available', 'phone_time_created', 'phone_time_updated'
    ]
    readonly_fields = ['get_image']
    search_fields = ['phone_brand', 'phone_model']
    list_filter = ['phone_model', 'phone_available', 'phone_time_created', 'phone_time_updated']
    list_editable = ['phone_price', 'phone_reserve', 'phone_available']
    prepopulated_fields = {'phone_slug': ('phone_model',)}

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.phone_image_1.url} width="50" height="50"')

    get_image.short_description = "Изображение"


class TabletAdmin(admin.ModelAdmin):
    list_display = [
        'tablet_brand', 'tablet_model', 'tablet_price', 'get_image',
        'tablet_reserve', 'tablet_available', 'tablet_time_created', 'tablet_time_updated'
    ]
    readonly_fields = ['get_image']
    search_fields = ['tablet_brand', 'tablet_model']
    list_filter = ['tablet_available', 'tablet_time_created', 'tablet_time_updated']
    list_editable = ['tablet_price', 'tablet_reserve', 'tablet_available']
    prepopulated_fields = {'tablet_slug': ('tablet_model',)}

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.tablet_image_1.url} width="50" height="50"')

    get_image.short_description = "Изображение"


class MotorOilAdmin(admin.ModelAdmin):
    list_display = [
        'm_oil_brand', 'm_oil_viscosity', 'm_oil_price', 'get_image',
        'm_oil_reserve', 'm_oil_available', 'm_oil_time_created', 'm_oil_time_updated'
    ]
    readonly_fields = ['get_image']
    search_fields = ['m_oil_brand', 'm_oil_model', 'm_oil_viscosity']
    list_filter = ['m_oil_available', 'm_oil_time_created', 'm_oil_time_updated']
    list_editable = ['m_oil_price', 'm_oil_reserve', 'm_oil_available']
    prepopulated_fields = {'m_oil_slug': ('m_oil_viscosity',)}

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.m_oil_image_1.url} width="50" height="50"')

    get_image.short_description = "Изображение"


class OilFilterAdmin(admin.ModelAdmin):
    list_display = [
        'oil_filter_brand', 'oil_filter_type', 'oil_filter_price', 'get_image',
        'oil_filter_reserve', 'oil_filter_available', 'oil_filter_time_created', 'oil_filter_time_updated'
    ]
    readonly_fields = ['get_image']
    search_fields = ['oil_filter_brand', 'oil_filter_type']
    list_filter = ['oil_filter_available', 'oil_filter_time_created', 'oil_filter_time_updated']
    list_editable = ['oil_filter_price', 'oil_filter_reserve', 'oil_filter_available']
    prepopulated_fields = {'oil_filter_slug': ('oil_filter_type',)}

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.oil_filter_image_1.url} width="50" height="50"')

    get_image.short_description = "Изображение"


admin.site.register(Phone, PhoneAdmin)
admin.site.register(Tablet, TabletAdmin)
admin.site.register(MotorOil, MotorOilAdmin)
admin.site.register(OilFilter, OilFilterAdmin)


class GoodCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class PhoneBrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class TabletBrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class MotorOilBrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class OilFilterBrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class OilFilterTypeAdmin(admin.ModelAdmin):
    list_display = ['type', 'slug']
    prepopulated_fields = {'slug': ('type',)}


admin.site.register(GoodCategory, GoodCategoryAdmin)
admin.site.register(PhoneBrand, PhoneBrandAdmin)
admin.site.register(TabletBrand, TabletBrandAdmin)
admin.site.register(MotorOilBrand, MotorOilBrandAdmin)
admin.site.register(OilFilterBrand, OilFilterBrandAdmin)
admin.site.register(OilFilterType, OilFilterTypeAdmin)
