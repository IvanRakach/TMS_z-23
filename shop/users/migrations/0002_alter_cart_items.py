# Generated by Django 3.2.9 on 2022-10-31 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_alter_product_category'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(blank=True, to='items.Item'),
        ),
    ]
