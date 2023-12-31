# Generated by Django 4.2.6 on 2023-11-01 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0019_apartment_side"),
    ]

    operations = [
        migrations.CreateModel(
            name="Stock",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("stock", models.CharField(max_length=255)),
                ("valid", models.CharField(max_length=255)),
                ("about", models.TextField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Акция",
                "verbose_name_plural": "Акции",
            },
        ),
    ]
