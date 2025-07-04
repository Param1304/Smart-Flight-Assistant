# Generated by Django 5.1.1 on 2025-04-26 19:04

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FlightDelayPrediction",
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
                ("airline", models.CharField(max_length=100)),
                ("origin", models.CharField(max_length=100)),
                ("destination", models.CharField(max_length=100)),
                ("month", models.IntegerField()),
                ("hour", models.IntegerField()),
                ("is_weekend", models.BooleanField()),
                ("day_of_month", models.IntegerField()),
                ("day_of_week", models.IntegerField()),
                ("prediction_result", models.FloatField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
