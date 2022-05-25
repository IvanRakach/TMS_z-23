import uuid

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    time_create = models.DateTimeField(auto_now_add=True, null=True)
    time_update = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class BooksGenre(models.Model):
    genre = models.CharField('Жанр книги', max_length=50)

    def __str__(self):
        return f"Book's genre {self.pk}. Жанр: {self.genre}"

    class Meta:
        verbose_name = "Жанр книги"
        verbose_name_plural = "Жанры книг"
        ordering = ["genre"]


class ClientsOrder(BaseModel):
    # slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    user = models.ForeignKey(
        User,
        max_length=50,
        on_delete=models.CASCADE,
        verbose_name="Логин пользователя",
    )
    books_category = models.ForeignKey(
        'BooksGenre',
        on_delete=models.CASCADE,
        verbose_name="Жанр книги",
    )
    user_name_private_room = models.CharField('Имя клиента', max_length=50)
    user_surname_private_room = models.CharField('Фамилия клиента', max_length=50)
    customers_passport_series = models.CharField('Серия паспорта клиента', max_length=2)
    customers_passport_number = models.CharField('Номер паспорта клиента', max_length=7)

    def __str__(self):
        return f"Client's order {self.pk}. Date: {self.user_name_private_room}"

    class Meta:
        verbose_name = "Заказ клиента"
        verbose_name_plural = "Заказы клиентов"
        ordering = ["user_name_private_room", "user_surname_private_room"]
