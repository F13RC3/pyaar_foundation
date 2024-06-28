# Generated by Django 5.0.6 on 2024-06-10 16:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Animal",
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
                ("Animal_category", models.CharField(max_length=200)),
                ("adopted_date", models.DateTimeField(verbose_name="Adoption Date")),
                ("category_id", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Details",
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
                ("category_details", models.CharField(max_length=200)),
                (
                    "category_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pyaar.animal"
                    ),
                ),
            ],
        ),
    ]