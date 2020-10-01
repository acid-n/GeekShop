from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='имя')
    description = models.TextField(blank=True, verbose_name='описание')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='категория')
    name = models.CharField(max_length=128, verbose_name='имя')
    image = models.ImageField(upload_to='products_images', blank=True, verbose_name='картинка')
    short_desc = models.CharField(max_length=128, blank=True, verbose_name='короткое описание')
    description = models.TextField(blank=True, verbose_name='полное описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='цена')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='количество')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return f'{self.name} ({self.category.name})'


class Contacts(models.Model):
    name = models.CharField(max_length=64, verbose_name="название", unique=True)
    city = models.CharField(max_length=64, verbose_name="город")
    email = models.CharField(max_length=64, verbose_name="email", unique=True)
    phone = models.CharField(max_length=64, verbose_name="телефон", unique=True)
    address = models.CharField(max_length=128, verbose_name="адрес", blank=True)

    class Meta:
        verbose_name = "контакты"
        verbose_name_plural = "контакты"

    def __str__(self):
        return f'{self.name} ({self.city})'
