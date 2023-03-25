from django.contrib.auth import get_user_model
from django.db import models


class Review(models.Model):
    author = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    product = models.ForeignKey(
        to='webapp.Product',
        on_delete=models.CASCADE,
        verbose_name='Товар'
    )
    text = models.TextField(
        max_length=3000,
        verbose_name='Текст'
    )
    rating = models.IntegerField(
        verbose_name='Оценка',
        choices=[
            (1, "1"),
            (2, "2"),
            (3, "3"),
            (4, "4"),
            (5, "5")
        ]
    )

    def __str__(self):
        return f"{self.author} - {self.product}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
