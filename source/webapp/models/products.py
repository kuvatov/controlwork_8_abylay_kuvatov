from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name='Товар'
    )
    category = models.CharField(
        max_length=100,
        verbose_name='Категория',
        choices=[
            ("foods", "Еда"),
            ("drinks", "Напитки"),
            ("clothes", "Одежда")
        ]
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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
