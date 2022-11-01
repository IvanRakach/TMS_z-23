from django.db import models


class BaseModel(models.Model):
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        abstract = True
