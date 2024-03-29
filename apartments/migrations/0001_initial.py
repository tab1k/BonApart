# Generated by Django 4.2.7 on 2024-02-16 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deal_type', models.CharField(choices=[('daily_rent', 'Аренда по суточно'), ('monthly_rent', 'Аренда помесячно'), ('sale', 'Продажа')], default='daily_rent', max_length=20, verbose_name='Тип сделки')),
                ('name', models.CharField(max_length=355, verbose_name='Название ЖК')),
                ('address', models.CharField(blank=True, max_length=355, null=True, verbose_name='Адрес ЖК')),
                ('description', models.TextField(verbose_name='Подробнее')),
                ('side', models.CharField(blank=True, choices=[('ala', 'Алматинский'), ('bai', 'Байконурский'), ('esil', 'Есильский'), ('nurin', 'Нуринский'), ('sary', 'Сарыаркинский')], max_length=10, null=True, verbose_name='Район')),
                ('level', models.CharField(blank=True, choices=[('lux', 'Люкс'), ('business', 'Бизнес'), ('prestige', 'Престиж')], max_length=10, null=True, verbose_name='Класс квартиры')),
                ('rating', models.IntegerField(blank=True, choices=[(1, '1 звезда'), (2, '2 звезды'), (3, '3 звезды'), (4, '4 звезды'), (5, '5 звезд')], null=True)),
                ('capacity', models.PositiveIntegerField(default=2, verbose_name='Вместимость')),
                ('room', models.PositiveIntegerField(default=1, verbose_name='Комнат')),
                ('square', models.PositiveIntegerField(default=37, verbose_name='Площадь')),
                ('floor', models.PositiveIntegerField(default=5, verbose_name='Этаж')),
                ('total_floors', models.PositiveSmallIntegerField(verbose_name='Кол-во этажей')),
                ('elevator', models.BooleanField(default=True, verbose_name='Лифт')),
                ('singlebeds', models.PositiveSmallIntegerField(default=1, verbose_name='Односпальных мест')),
                ('doublebeds', models.PositiveSmallIntegerField(default=1, verbose_name='Двухспальных мест')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='apartment_images/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='apartment_images/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='apartment_images/')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='apartment_images/')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='apartment_images/')),
                ('image6', models.ImageField(blank=True, null=True, upload_to='apartment_images/')),
                ('image7', models.ImageField(blank=True, null=True, upload_to='apartment_images/')),
                ('image8', models.ImageField(blank=True, null=True, upload_to='apartment_images/')),
                ('image9', models.ImageField(blank=True, null=True, upload_to='apartment_images/')),
                ('image10', models.ImageField(blank=True, null=True, upload_to='apartment_images/')),
                ('image11', models.ImageField(blank=True, null=True, upload_to='apartment_images/')),
                ('image12', models.ImageField(blank=True, null=True, upload_to='apartment_images/')),
                ('wifi', models.BooleanField(default=False, verbose_name='Wi-Fi')),
                ('air_conditioning', models.BooleanField(default=False, verbose_name='Кондиционер')),
                ('parking', models.BooleanField(default=False, verbose_name='Платный паркинг')),
                ('bath', models.BooleanField(default=False, verbose_name='Ванна')),
                ('orthopedic_mattress', models.BooleanField(default=False, verbose_name='Ортопедический матрац')),
                ('smart_tv', models.BooleanField(default=False, verbose_name='Smart TV')),
                ('hairdryer', models.BooleanField(default=False, verbose_name='Фен')),
                ('iron', models.BooleanField(default=False, verbose_name='Утюг')),
                ('washing_machine', models.BooleanField(default=False, verbose_name='Стиральная машинка')),
            ],
            options={
                'verbose_name': 'Квартира',
                'verbose_name_plural': 'Квартиры',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('surname', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('phone', models.CharField(max_length=20, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
        migrations.CreateModel(
            name='GeoPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='geo_images')),
                ('link', models.TextField(blank=True, null=True)),
                ('apartment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apartments.apartment', verbose_name='ЖК')),
            ],
            options={
                'verbose_name': 'Геопозиция дома',
                'verbose_name_plural': 'Геопозиции домов',
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_count', models.IntegerField(blank=True, null=True, verbose_name='Скидка')),
                ('apartment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apartments.apartment', verbose_name='ЖК')),
            ],
            options={
                'verbose_name': 'Скидка',
                'verbose_name_plural': 'Скидки',
            },
        ),
    ]
