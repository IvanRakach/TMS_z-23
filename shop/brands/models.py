from django.db import models

from utils.models import BaseModel


class Brand (BaseModel):
    brand_name = models.CharField(max_length=200, unique=True, verbose_name='Бренд')
    brand_foundation_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.brand_name}'
