# Generated by Django 4.2.6 on 2023-10-29 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0017_reservation"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="reservation",
            name="apartment",
        ),
    ]
