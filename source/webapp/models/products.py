from django.db import models
from django.db.models import TextChoices
from django.utils import timezone


class CategoryChoice(TextChoices):
    FOOD = 'foods', 'Еда'
    CLOTHING = 'clothes', 'Одежда'
    DRINKS = 'drinks', 'Напитки'
    OTHER = 'other', 'Разное'


class Product(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name='Товар'
    )
    category = models.CharField(
        max_length=100,
        verbose_name='Категория',
        choices=CategoryChoice.choices,
        default=CategoryChoice.OTHER
    )
    description = models.TextField(
        max_length=3000,
        blank=True,
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to="product_images",
        blank=True,
        verbose_name='Картинка'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время добавления"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления"
    )
    is_deleted = models.BooleanField(
        null=False,
        default=False,
        verbose_name="Удален"
    )
    deleted_at = models.DateTimeField(
        null=True,
        default=None,
        verbose_name="Дата и время удаления"
    )

    def __str__(self):
        return self.name

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_date = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
