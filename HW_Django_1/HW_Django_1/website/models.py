from django.db import models


class Authors(models.Model):
    first_name = models.CharField('Имя автора', max_length=50)
    last_name = models.CharField('Фамилия автора', max_length=50)
    date_of_birth = models.CharField('Дата рождения', max_length=10)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания записи')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления записи')

    def __str__(self):
        return str(self.first_name)

    class Meta:
        verbose_name = '''Таблица: Автор'''
        verbose_name_plural = '''Таблица: Авторы'''
        ordering = ['first_name', 'last_name', '-time_create']


class Books(models.Model):
    book_name = models.CharField('Наименование книги', max_length=100)
    publ_year = models.CharField('Год публикации', max_length=4)
    book_image = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фотография')  # blank=True
    book_price_BYN = models.PositiveIntegerField('Цена в BYN')  # , max_length=15
    authors_fk = models.ForeignKey('Authors', max_length=50, on_delete=models.CASCADE,
                                   verbose_name="Автор")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания объявления')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления объявления')

    def __str__(self):
        return str(self.book_name)

    class Meta:
        verbose_name = '''Таблица: Книга'''
        verbose_name_plural = '''Таблица: Книги'''
        ordering = ['book_name', 'book_price_BYN', 'authors_fk', '-time_create']
