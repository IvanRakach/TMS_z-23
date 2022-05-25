from django.contrib import admin

from private_room.models import *


class BooksGenreAdmin(admin.ModelAdmin):
    # список полей, которые мы хотим видеть в нашей админ панели
    list_display = \
        (
            'id',
            'genre',
        )
    # те поля, на которые мы можем кликнуть и перейти на соответствующий отзыв
    list_display_links = \
        (
            'id',
            'genre',
        )
    # те поля, по которым мы можем производить поиск информации
    search_fields = \
        (
            'genre',
        )


admin.site.register(BooksGenre, BooksGenreAdmin)


class ClientsOrderAdmin(admin.ModelAdmin):
    # список полей, которые мы хотим видеть в нашей админ панели
    list_display = \
        (
            'id',
            'user',
            'books_category',
            'user_name_private_room',
            'user_surname_private_room',
            'customers_passport_series',
            'customers_passport_number',
            'time_create',
            'time_update',
        )
    # те поля, на которые мы можем кликнуть и перейти на соответствующий отзыв
    list_display_links = \
        (
            'id',
            'user',
            'user_name_private_room',
            'user_surname_private_room',
        )
    # те поля, по которым мы можем производить поиск информации
    search_fields = \
        (
            'user_name_private_room',
            'user_surname_private_room',
            'time_create',
        )
    # те поля, по которым мы можем фильтровать список статей
    list_filter = \
        (
            'books_category',
            'user_surname_private_room',
            'time_create',
            'time_update',
        )


admin.site.register(ClientsOrder, ClientsOrderAdmin)
