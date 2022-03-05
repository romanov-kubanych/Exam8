from django.contrib.auth import get_user_model
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время обновления")


User = get_user_model()
STATUS_CHOICES = [('other', 'Разное'), ('smartphone', 'Смартфон'), ('notebook', 'Ноутбук'), ('tv', 'Телевизор')]


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    category = models.CharField(max_length=100,
                                choices=STATUS_CHOICES,
                                default=STATUS_CHOICES[0][0],
                                verbose_name='Категория')
    description = models.TextField(max_length=2000, verbose_name='Описание', null=True, blank=True)
    picture = models.ImageField(null=True,
                                blank=True,
                                upload_to='product_pics',
                                verbose_name='Картинка')

    def __str__(self):
        return f'{self.pk}.{self.name} - {self.category}'

    class Meta:
        db_table = 'Products'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Review(BaseModel):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               default=1,
                               verbose_name='Автор',
                               related_name='reviews')
    product = models.ForeignKey('webapp.Product',
                                on_delete=models.CASCADE,
                                verbose_name='Товар',
                                related_name='reviews')
    text = models.TextField(max_length=2000, verbose_name='Текст отзыва')
    grade = models.IntegerField(verbose_name='Оценка')
    status = models.BooleanField(verbose_name='Статус', default=False)

    def __str__(self):
        return f'{self.pk}.{self.grade} - {self.author.username}'

    class Meta:
        db_table = 'Reviews'
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
