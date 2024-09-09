# Generated by Django 5.0.7 on 2024-07-15 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cuidar", "0002_medicamento_patologia_paciente_medicamentos_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="DiaSemana",
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
                (
                    "dia",
                    models.CharField(
                        choices=[
                            ("SEG", "Segunda-feira"),
                            ("TER", "Terça-feira"),
                            ("QUA", "Quarta-feira"),
                            ("QUI", "Quinta-feira"),
                            ("SEX", "Sexta-feira"),
                            ("SAB", "Sábado"),
                            ("DOM", "Domingo"),
                        ],
                        max_length=3,
                        unique=True,
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="medicamento",
            name="horario",
            field=models.TimeField(),
        ),
        migrations.AddField(
            model_name="medicamento",
            name="dias_semana",
            field=models.ManyToManyField(
                related_name="medicamento", to="cuidar.diasemana"
            ),
        ),
    ]