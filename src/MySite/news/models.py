from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        null=True,
        verbose_name='Категория'
    )

    def my_func(self):
        return 'Последние новости'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Products(models.Model):
    name = models.CharField(max_length=150)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(null=True, default=1)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    in_stock = models.BooleanField(default=True)

    # Метод, чтобы объекты при работе с ORM
    # отображались со своими именами
    # def __str__(self):
    #     return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя врача')
    spec = models.CharField(max_length=50, verbose_name='Специализация')
    cabinet = models.PositiveIntegerField(verbose_name='Кабинет')

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'
        ordering = ['name']

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя пациента')
    birth_date = models.DateField(verbose_name='Дата рождения')
    telephone = models.PositiveIntegerField(max_length=11, verbose_name='Номер телефона')
    diagnosis = models.CharField(max_length=100, verbose_name='Диагноз')
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Врач'
    )

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'
        ordering = ['name']
