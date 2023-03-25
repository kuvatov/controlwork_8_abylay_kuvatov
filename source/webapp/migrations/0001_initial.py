# Generated by Django 4.1.7 on 2023-03-25 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30, verbose_name="Товар")),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("foods", "Еда"),
                            ("drinks", "Напитки"),
                            ("clothes", "Одежда"),
                        ],
                        max_length=100,
                        verbose_name="Категория",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, max_length=3000, verbose_name="Описание"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, upload_to="product_images", verbose_name="Картинка"
                    ),
                ),
            ],
        ),
    ]