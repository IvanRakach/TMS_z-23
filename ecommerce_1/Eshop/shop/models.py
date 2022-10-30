from django.db import models


class Phone(models.Model):
    category = models.ForeignKey('GoodCategory', on_delete=models.PROTECT, related_name='phones')
    phone_brand = models.ForeignKey('PhoneBrand', max_length=50, on_delete=models.PROTECT, db_index=True,
                                    verbose_name='Бренд')
    phone_model = models.CharField(max_length=200, db_index=True, verbose_name='Модель')
    phone_slug = models.SlugField(max_length=200, db_index=True)
    phone_release_date = models.PositiveIntegerField(verbose_name='Год выпуска')
    phone_operating_system = models.CharField(max_length=200, db_index=True, verbose_name='Операционная система')
    phone_operating_system_version = models.CharField(max_length=200, db_index=True,
                                                      verbose_name='Версия операционной системы')
    phone_communication_standards_support = models.CharField(max_length=200, db_index=True,
                                                             verbose_name='Поддержка стандартов связи')
    phone_description = models.TextField(blank=True, null=True)
    phone_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена, BYN')
    phone_image_1 = models.ImageField(upload_to='phones/%Y/%m/%d', verbose_name='Фотография 1', blank=True, null=True)
    phone_image_2 = models.ImageField(upload_to='phones/%Y/%m/%d', verbose_name='Фотография 2', blank=True, null=True)
    phone_image_3 = models.ImageField(upload_to='phones/%Y/%m/%d', verbose_name='Фотография 3', blank=True, null=True)
    phone_image_4 = models.ImageField(upload_to='phones/%Y/%m/%d', verbose_name='Фотография 4', blank=True, null=True)
    phone_image_5 = models.ImageField(upload_to='phones/%Y/%m/%d', verbose_name='Фотография 5', blank=True, null=True)
    phone_video_youtube = models.CharField(null=True, blank=True, max_length=255,
                                           verbose_name='Видео (ссылка на YouTube)')
    phone_reserve = models.PositiveIntegerField(verbose_name='Запасы')
    phone_available = models.BooleanField(default=True, verbose_name='Доступен к продаже')
    phone_time_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания карточки')
    phone_time_updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения карточки')

    class Meta:
        ordering = ('phone_model',)
        index_together = (('id', 'phone_slug'),)
        verbose_name = 'Карта телефона'
        verbose_name_plural = 'Каталог телефонов'

    def __str__(self):
        return self.phone_model


class Tablet(models.Model):
    category = models.ForeignKey('GoodCategory', on_delete=models.PROTECT, related_name='tablets')
    tablet_brand = models.ForeignKey('TabletBrand', max_length=50, on_delete=models.PROTECT, db_index=True,
                                     verbose_name='Бренд')
    tablet_model = models.CharField(max_length=200, db_index=True, verbose_name='Модель')
    tablet_slug = models.SlugField(max_length=200, db_index=True)
    tablet_release_date = models.PositiveIntegerField(verbose_name='Год выпуска')
    tablet_operating_system = models.CharField(max_length=200, db_index=True, verbose_name='Операционная система')
    tablet_operating_system_version = models.CharField(max_length=200, db_index=True,
                                                       verbose_name='Версия операционной системы')
    tablet_dual_sim_support = models.CharField(max_length=200, db_index=True,
                                               verbose_name='Поддержка двух SIM-карт')
    tablet_description = models.TextField(blank=True, null=True, verbose_name='описание')
    tablet_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена, BYN')
    tablet_image_1 = models.ImageField(upload_to='tablets/%Y/%m/%d', verbose_name='Фотография 1', blank=True,
                                       null=True)
    tablet_image_2 = models.ImageField(upload_to='tablets/%Y/%m/%d', verbose_name='Фотография 2', blank=True,
                                       null=True)
    tablet_image_3 = models.ImageField(upload_to='tablets/%Y/%m/%d', verbose_name='Фотография 3', blank=True,
                                       null=True)
    tablet_image_4 = models.ImageField(upload_to='tablets/%Y/%m/%d', verbose_name='Фотография 4', blank=True,
                                       null=True)
    tablet_image_5 = models.ImageField(upload_to='tablets/%Y/%m/%d', verbose_name='Фотография 5', blank=True,
                                       null=True)
    tablet_video_youtube = models.CharField(null=True, blank=True, max_length=255,
                                            verbose_name='Видео (ссылка на YouTube)')
    tablet_reserve = models.PositiveIntegerField(verbose_name='Запасы')
    tablet_available = models.BooleanField(default=True, verbose_name='Доступен к продаже')
    tablet_time_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания карточки')
    tablet_time_updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения карточки')

    class Meta:
        ordering = ('tablet_model',)
        index_together = (('id', 'tablet_slug'),)
        verbose_name = 'Карта планшета'
        verbose_name_plural = 'Каталог планшетов'

    def __str__(self):
        return self.tablet_model


class MotorOil(models.Model):
    category = models.ForeignKey('GoodCategory', on_delete=models.PROTECT, related_name='motor_oils')
    m_oil_brand = models.ForeignKey('MotorOilBrand', max_length=50, on_delete=models.PROTECT, db_index=True,
                                    verbose_name='Бренд')
    m_oil_viscosity = models.CharField(max_length=200, db_index=True, verbose_name='Вязкость')
    m_oil_slug = models.SlugField(max_length=200, db_index=True)
    m_oil_volume = models.PositiveIntegerField(verbose_name='Объем упаковки, литров')
    m_oil_description = models.TextField(blank=True, null=True, verbose_name='Описание')
    m_oil_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена, BYN')
    m_oil_image_1 = models.ImageField(upload_to='motor_oils/%Y/%m/%d', verbose_name='Фотография 1', blank=True,
                                      null=True)
    m_oil_reserve = models.PositiveIntegerField(verbose_name='Запасы')
    m_oil_available = models.BooleanField(default=True, verbose_name='Доступен к продаже')
    m_oil_time_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания карточки')
    m_oil_time_updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения карточки')

    class Meta:
        ordering = ('m_oil_brand',)
        index_together = (('id', 'm_oil_slug'),)
        verbose_name = 'Карта моторного масла'
        verbose_name_plural = 'Каталог моторных масел'

    def __str__(self):
        return self.m_oil_viscosity


class OilFilter(models.Model):
    category = models.ForeignKey('GoodCategory', on_delete=models.PROTECT, related_name='oil_filters')
    oil_filter_brand = models.ForeignKey('OilFilterBrand', max_length=50, on_delete=models.PROTECT, db_index=True,
                                         verbose_name='Бренд масляного фильтра')
    oil_filter_slug = models.SlugField(max_length=200, db_index=True)
    oil_filter_type = models.ForeignKey('OilFilterType', max_length=100, on_delete=models.PROTECT, db_index=True,
                                        verbose_name='Тип масляного фильтра')
    oil_filter_external_diameter = models.CharField(max_length=200, db_index=True)
    oil_filter_height = models.CharField(max_length=200, db_index=True)
    oil_filter_thread = models.CharField(max_length=200, db_index=True)
    oil_filter_suitable_for_cars = models.CharField(max_length=200, db_index=True)
    oil_filter_description = models.TextField(blank=True, null=True)
    oil_filter_price = models.DecimalField(max_digits=10, decimal_places=2)
    oil_filter_image_1 = models.ImageField(upload_to='oil_filters/%Y/%m/%d', verbose_name='Фотография 1', blank=True,
                                           null=True)
    oil_filter_reserve = models.PositiveIntegerField()
    oil_filter_available = models.BooleanField(default=True)
    oil_filter_time_created = models.DateTimeField(auto_now_add=True)
    oil_filter_time_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('oil_filter_brand',)
        index_together = (('id', 'oil_filter_slug'),)
        verbose_name = 'Карта масляного фильтра'
        verbose_name_plural = 'Каталог масляных фильтров'

    def __str__(self):
        return self.oil_filter_brand


class GoodCategory(models.Model):
    name = models.CharField(max_length=200, db_index=True, unique=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'

    def __str__(self):
        return self.name


class PhoneBrand(models.Model):
    name = models.CharField(max_length=200, db_index=True, unique=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Бренд телефона'
        verbose_name_plural = 'Бренды телефонов'

    def __str__(self):
        return self.name


class TabletBrand(models.Model):
    name = models.CharField(max_length=200, db_index=True, unique=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Бренд планшета'
        verbose_name_plural = 'Бренды планшетов'

    def __str__(self):
        return self.name


class MotorOilBrand(models.Model):
    name = models.CharField(max_length=200, db_index=True, unique=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Бренд моторного масла'
        verbose_name_plural = 'Бренды моторных масел'

    def __str__(self):
        return self.name


class OilFilterBrand(models.Model):
    name = models.CharField(max_length=200, db_index=True, unique=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Бренд масляного фильтра'
        verbose_name_plural = 'Бренды масляных фильтров'

    def __str__(self):
        return self.name


class OilFilterType(models.Model):
    type = models.CharField(max_length=200, db_index=True, unique=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('type',)
        verbose_name = 'Тип масляного фильтра'
        verbose_name_plural = 'Типы масляных фильтров'

    def __str__(self):
        return self.type
