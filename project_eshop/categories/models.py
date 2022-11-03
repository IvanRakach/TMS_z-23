from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


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
