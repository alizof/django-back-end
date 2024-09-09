# Generated by Django 5.0.7 on 2024-07-14 21:59

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Paciente",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("nome", models.CharField(max_length=150)),
                ("cip", models.CharField(max_length=17)),
                ("created_at", models.DateField(auto_now=True)),
            ],
        ),
    ]