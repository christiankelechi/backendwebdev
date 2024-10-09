# Generated by Django 5.0.6 on 2024-10-09 13:51

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ClassList",
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
                ("first_name", models.CharField(max_length=2000)),
                ("last_name", models.CharField(max_length=4000)),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=4000, null=True),
                ),
            ],
        ),
    ]
