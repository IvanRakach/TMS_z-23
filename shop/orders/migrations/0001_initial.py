# Generated by Django 3.2.9 on 2022-10-31 23:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('items', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('IN_PROGRESS', 'In progress'), ('DELIVERED', 'Delivered')], default='PENDING', max_length=25)),
                ('items', models.ManyToManyField(related_name='orders', to='items.Item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
