# Generated by Django 4.2.7 on 2024-02-28 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0012_apartment_dishes_apartment_electric_kettle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='video',
            field=models.URLField(blank=True, null=True, verbose_name='Видео-ролик'),
        ),
    ]