# Generated by Django 4.1.7 on 2023-03-25 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("webapp", "0002_review"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={"verbose_name": "Товар", "verbose_name_plural": "Товары"},
        ),
        migrations.AlterModelOptions(
            name="review",
            options={"verbose_name": "Отзыв", "verbose_name_plural": "Отзывы"},
        ),
    ]