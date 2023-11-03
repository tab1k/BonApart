# Generated by Django 4.2.6 on 2023-10-28 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Apartment",
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
                ("name", models.CharField(max_length=355)),
                ("description", models.TextField()),
                ("capacity", models.PositiveIntegerField(default=2)),
                ("room", models.PositiveIntegerField(default=1)),
                ("square", models.PositiveIntegerField(default=37)),
                ("floor", models.PositiveIntegerField(default=5)),
                ("total_floors", models.PositiveSmallIntegerField()),
                ("elevator", models.BooleanField(default=True)),
                ("singlebeds", models.PositiveSmallIntegerField(default=1)),
                ("doublebeds", models.PositiveSmallIntegerField(default=1)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("wifi", models.BooleanField(default=False)),
                ("air_conditioning", models.BooleanField(default=False)),
                ("parking", models.BooleanField(default=False)),
                ("bath", models.BooleanField(default=False)),
                ("orthopedic_mattress", models.BooleanField(default=False)),
                ("smart_tv", models.BooleanField(default=False)),
                ("hairdryer", models.BooleanField(default=False)),
                ("iron", models.BooleanField(default=False)),
                ("washing_machine", models.BooleanField(default=False)),
            ],
        ),
    ]