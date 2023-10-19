# Generated by Django 4.2.6 on 2023-10-19 13:01

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="News",
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
                ("image_url", models.URLField(blank=True, max_length=500, null=True)),
                ("title", models.CharField(blank=True, max_length=500, null=True)),
                (
                    "link_address",
                    models.URLField(blank=True, max_length=500, null=True),
                ),
            ],
        ),
    ]
