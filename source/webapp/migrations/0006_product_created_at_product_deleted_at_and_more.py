# Generated by Django 4.1.7 on 2023-03-25 11:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("webapp", "0005_alter_review_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Дата и время добавления",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="deleted_at",
            field=models.DateTimeField(
                default=None, null=True, verbose_name="Дата и время удаления"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="is_deleted",
            field=models.BooleanField(default=False, verbose_name="Удален"),
        ),
        migrations.AddField(
            model_name="product",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, verbose_name="Дата и время обновления"
            ),
        ),
        migrations.AddField(
            model_name="review",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Дата и время добавления",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="review",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, verbose_name="Дата и время обновления"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.CharField(
                choices=[
                    ("foods", "Еда"),
                    ("clothes", "Одежда"),
                    ("drinks", "Напитки"),
                    ("other", "Разное"),
                ],
                default="other",
                max_length=100,
                verbose_name="Категория",
            ),
        ),
    ]
