# Generated by Django 4.2.7 on 2023-11-22 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0024_remove_geoposition_latitude_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="apartment",
            name="image10",
            field=models.ImageField(
                blank=True, null=True, upload_to="apartment_images/"
            ),
        ),
        migrations.AddField(
            model_name="apartment",
            name="image11",
            field=models.ImageField(
                blank=True, null=True, upload_to="apartment_images/"
            ),
        ),
        migrations.AddField(
            model_name="apartment",
            name="image12",
            field=models.ImageField(
                blank=True, null=True, upload_to="apartment_images/"
            ),
        ),
        migrations.AddField(
            model_name="apartment",
            name="image6",
            field=models.ImageField(
                blank=True, null=True, upload_to="apartment_images/"
            ),
        ),
        migrations.AddField(
            model_name="apartment",
            name="image7",
            field=models.ImageField(
                blank=True, null=True, upload_to="apartment_images/"
            ),
        ),
        migrations.AddField(
            model_name="apartment",
            name="image8",
            field=models.ImageField(
                blank=True, null=True, upload_to="apartment_images/"
            ),
        ),
        migrations.AddField(
            model_name="apartment",
            name="image9",
            field=models.ImageField(
                blank=True, null=True, upload_to="apartment_images/"
            ),
        ),
    ]
