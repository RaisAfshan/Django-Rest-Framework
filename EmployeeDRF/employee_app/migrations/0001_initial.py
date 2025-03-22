# Generated by Django 5.1.7 on 2025-03-15 05:11

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
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
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "department",
                    models.IntegerField(
                        choices=[(1, "Human Resources"), (2, "IT"), (3, "Finance")],
                        default=1,
                    ),
                ),
                ("salary", models.DecimalField(decimal_places=2, max_digits=10)),
                ("data_joined", models.DateField(auto_now_add=True)),
                ("profile_pic", models.FileField(upload_to="uploads/")),
            ],
        ),
    ]
