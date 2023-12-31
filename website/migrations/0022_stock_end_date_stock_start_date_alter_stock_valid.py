# Generated by Django 4.2.6 on 2023-11-01 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0021_alter_reservation_options_stock_photo"),
    ]

    operations = [
        migrations.AddField(
            model_name="stock",
            name="end_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="stock",
            name="start_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="stock",
            name="valid",
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
