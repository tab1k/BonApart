# Generated by Django 4.2.7 on 2024-03-26 10:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apartments", "0014_remove_apartment_level_alter_apartment_room"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="apartment",
            name="rating",
        ),
        migrations.AlterField(
            model_name="apartment",
            name="room",
            field=models.PositiveIntegerField(
                choices=[("1", "1"), ("2", "2"), ("3", "3"), ("4", "4")],
                verbose_name="Комнат",
            ),
        ),
    ]
