# Generated by Django 4.2.7 on 2024-02-22 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0007_apartmentstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='status',
            field=models.CharField(choices=[('pending', 'На рассмотрении'), ('approved', 'Одобрено'), ('rejected', 'Отклонено')], default='pending', max_length=20),
        ),
    ]
