# Generated by Django 4.2.6 on 2023-10-28 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0006_car_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="image",
            field=models.ImageField(upload_to="images/", verbose_name="Фотография"),
        ),
    ]
