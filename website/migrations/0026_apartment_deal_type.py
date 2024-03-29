# Generated by Django 4.2.7 on 2024-02-15 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0025_apartment_image10_apartment_image11_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='deal_type',
            field=models.CharField(choices=[('daily_rent', 'Аренда по суточно'), ('monthly_rent', 'Аренда помесячно'), ('sale', 'Продажа')], default='daily_rent', max_length=20, verbose_name='Тип сделки'),
        ),
    ]
