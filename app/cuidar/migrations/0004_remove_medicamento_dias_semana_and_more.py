# Generated by Django 5.0.7 on 2024-07-15 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cuidar", "0003_diasemana_alter_medicamento_horario_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="medicamento",
            name="dias_semana",
        ),
        migrations.RemoveField(
            model_name="medicamento",
            name="horario",
        ),
        migrations.AddField(
            model_name="medicamento",
            name="descricao",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="patologia",
            name="descricao",
            field=models.TextField(default=""),
        ),
    ]
