# Generated by Django 4.2.6 on 2023-10-28 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0002_alter_apartment_options_apartment_level_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="apartment",
            name="address",
            field=models.CharField(
                blank=True, max_length=355, null=True, verbose_name="Адрес ЖК"
            ),
        ),
        migrations.AlterField(
            model_name="apartment",
            name="name",
            field=models.CharField(max_length=355, verbose_name="Название ЖК"),
        ),
    ]