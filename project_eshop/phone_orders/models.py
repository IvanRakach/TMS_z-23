from django.db import models
from django.contrib.auth.models import User

from utils.models import BaseModel

ORDER_CHOICES = [
    ('PENDING', 'Pending'),
    ('IN_PROGRESS', 'In progress'),
    ('DELIVERED', 'Delivered'),
]


class Order(BaseModel):
    items = models.ManyToManyField('phone_items.Item', related_name='order')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='orders')
    status = models.CharField(max_length=25, choices=ORDER_CHOICES, default='PENDING')

    def __str__(self):
        return f'User order: {self.user}. User item: {self.items}'
