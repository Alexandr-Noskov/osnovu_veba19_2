from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f'({self.name} {self.description})'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    image = models.ImageField(verbose_name='изображение (превью)', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    unit_price = models.IntegerField(verbose_name='цена за покупку')
    produce_day = models.DateField(verbose_name='дата создания')
    last_change = models.DateField(verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='товар')
    version = models.IntegerField(verbose_name='номер версии')
    name_version = models.CharField(max_length=100, verbose_name='название версии')
    is_active = models.BooleanField(default=True, verbose_name='активна')

    def __str__(self):
        return f'{self.product.name} {self.version} {self.is_active}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'