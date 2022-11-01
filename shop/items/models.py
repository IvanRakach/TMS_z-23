from django.core.validators import MinValueValidator
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from rest_framework.reverse import reverse

from utils.models import BaseModel


class Category(MPTTModel):
    name = models.CharField(max_length=100, unique=True, verbose_name='Категория')
    # self используется для того, чтобы ссылаться на ту же самую модель (поле id родителя)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                            related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name}'

    # def get_absolute_url(self):
    #     return reverse('', kwargs={'pk': self.pk})


class Product(BaseModel):
    brand = models.ForeignKey('brands.Brand', on_delete=models.PROTECT, related_name='products')
    category = TreeForeignKey('Category', on_delete=models.PROTECT, related_name='products')
    product_name = models.CharField(max_length=200, verbose_name='Наименование продукта')
    product_description = models.TextField(blank=True, null=True)
    product_image_1 = models.ImageField(upload_to='items/%Y/%m/%d', verbose_name='Фотография 1',
                                        blank=True, null=True)

    def __str__(self):
        return f'Product: {self.product_name}'


class Item(BaseModel):
    product = models.ForeignKey('Product', on_delete=models.PROTECT, related_name='items')
    serial_number = models.CharField(max_length=200, blank=True, null=True, unique=True, verbose_name='Серийный номер')
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)],
                                verbose_name='Цена, BYN')
    is_available = models.BooleanField(default=True, verbose_name='Доступен к продаже')

    class Meta:
        verbose_name_plural = 'Items'

    def __str__(self):
        return f'Serial number: {self.serial_number}. Product: {self.product.product_name}. ' \
               f'Price: {self.price}'
