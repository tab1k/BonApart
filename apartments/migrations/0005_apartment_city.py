# Generated by Django 4.2.7 on 2024-02-22 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0004_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apartments.city', verbose_name='Города'),
        ),
    ]