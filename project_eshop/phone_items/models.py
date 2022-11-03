from django.core.validators import MinValueValidator
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from rest_framework.reverse import reverse

from utils.models import BaseModel
from categories.models import Category


class Brand(BaseModel):
    name = models.CharField(max_length=200, unique=True, verbose_name='Бренд')

    # brand_foundation_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class Product(BaseModel):
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT, related_name='products')
    category = TreeForeignKey('categories.Category', on_delete=models.PROTECT, related_name='products')
    name = models.CharField(max_length=200, verbose_name='Наименование продукта')
    description = models.TextField(blank=True, null=True)
    param = models.TextField(blank=True, null=True)
    image_1 = models.ImageField(upload_to='phone_items/%Y/%m/%d', verbose_name='Фотография 1',
                                blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'Product: {self.name}'


class Item(BaseModel):
    product = models.ForeignKey('Product', on_delete=models.PROTECT, related_name='items')
    serial_number = models.CharField(max_length=200, blank=True, null=True, unique=True,
                                     verbose_name='Серийный номер')
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)],
                                verbose_name='Цена, BYN')
    is_available = models.BooleanField(default=True, verbose_name='Доступен к продаже')

    class Meta:
        verbose_name_plural = 'Items'

    def __str__(self):
        return f'Serial number: {self.serial_number}. Product: {self.product.name}. ' \
               f'Price: {self.price}'
