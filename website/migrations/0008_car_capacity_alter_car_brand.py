# Generated by Django 4.2.6 on 2023-10-28 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0007_alter_car_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="capacity",
            field=models.SmallIntegerField(
                blank=True, null=True, verbose_name="Вместительность"
            ),
        ),
        migrations.AlterField(
            model_name="car",
            name="brand",
            field=models.CharField(max_length=255, verbose_name="Бренд"),
        ),
    ]
