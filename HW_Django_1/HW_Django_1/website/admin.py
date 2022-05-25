from django.contrib import admin
from .models import *


class AuthorsAdmin(admin.ModelAdmin):
    # список полей, которые мы хотим видеть в нашей админ панели
    list_display = \
        (
            'id',
            'first_name',
            'last_name',
            'date_of_birth',
        )
    # те поля, на которые мы можем кликнуть и перейти на соответствующий отзыв
    list_display_links = \
        (
            'id',
            'first_name',
            'last_name',
        )
    # те поля, по которым мы можем производить поиск информации
    search_fields = \
        (
            'first_name',
            'last_name',
            'date_of_birth',
        )
    # те поля, по которым мы можем фильтровать список статей
    list_filter = ('time_create',)


admin.site.register(Authors, AuthorsAdmin)


class BooksAdmin(admin.ModelAdmin):
    # список полей, которые мы хотим видеть в нашей админ панели
    list_display = \
        (
            'id',
            'book_name',
            'publ_year',
            'book_image',
            'book_price_BYN',
            'authors_fk',
        )
    # те поля, на которые мы можем кликнуть и перейти на соответствующий отзыв
    list_display_links = \
        (
            'id',
            'book_name',
            'book_price_BYN',
        )
    # те поля, по которым мы можем производить поиск информации
    search_fields = \
        (
            'book_name',
            'publ_year',
            'book_price_BYN',
        )
    # те поля, по которым мы можем фильтровать список статей
    list_filter = ('time_create',)


admin.site.register(Books, BooksAdmin)


class SalesAdmin(admin.ModelAdmin):
    # список полей, которые мы хотим видеть в нашей админ панели
    list_display = \
        (
            'id',
            'header',
            'text',
            'image_field',
            'time_create',
            'time_update',
        )
    # те поля, на которые мы можем кликнуть и перейти на соответствующий отзыв
    list_display_links = \
        (
            'id',
            'header',
            'text',
            'image_field',
        )
    # те поля, по которым мы можем производить поиск информации
    search_fields = \
        (
            'header',
            'text',
        )
    # те поля, по которым мы можем фильтровать список статей
    list_filter = \
        (
            'time_create', 
            'time_update',
        )


admin.site.register(Sales, SalesAdmin)
