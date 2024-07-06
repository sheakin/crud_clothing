# Generated by Django 5.0.4 on 2024-07-06 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="A_User",
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
                ("name", models.CharField(max_length=100)),
                ("age", models.PositiveIntegerField()),
                ("place", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
    ]
