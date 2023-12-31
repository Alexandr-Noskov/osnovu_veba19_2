from config import settings
from django.db import models

NULLABLE = {
    'null': True,
    'blank': True
}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    # created_at = models.DateTimeField(verbose_name='Дата создания')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    STATUS_CREATED = 'created'
    STATUS_MODERATED = 'moderated'
    STATUS_PUBLISH = 'published'
    STATUSES = (
        (STATUS_CREATED, 'Добавлен'),
        (STATUS_MODERATED, 'На модерации'),
        (STATUS_PUBLISH, 'Опубликован'),
    )

    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    image = models.ImageField(upload_to='catalog/', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Стоимость')
    created_at = models.DateTimeField(**NULLABLE, auto_now_add=True, verbose_name='Дата создания')
    mod_at = models.DateTimeField(**NULLABLE, auto_now=True, verbose_name='Дата изменения')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='продавец', **NULLABLE)
    status = models.CharField(max_length=20, choices=STATUSES, default=STATUS_MODERATED, verbose_name='статус')

    def __str__(self):
        return f'{self.name} ({self.price})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        permissions = [
            ('set_product_status', 'Can change the status of products'),
            ('change_product_description', 'Can change product description'),
            ('change_product_category', 'Can change product category'),
        ]


class Contacts(models.Model):
    phone = models.CharField(max_length=30, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Email')
    address = models.CharField(max_length=200, verbose_name='Адрес')
    schedule = models.CharField(max_length=100, verbose_name='График работы')

    def __str__(self):
        return f'{self.phone}, {self.email}, {self.address}, {self.schedule}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    version_num = models.CharField(max_length=20, verbose_name='Номер версии')
    version_name = models.CharField(max_length=150, verbose_name='Название версии')
    version_activ = models.BooleanField(default=False, verbose_name='Текущая версия')

    def __str__(self):
        return f'{self.product} - {self.version_num}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'