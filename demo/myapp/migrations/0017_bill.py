# Generated by Django 5.0 on 2024-04-20 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0016_alter_medicalreport_medicine_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Bill",
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
                ("name", models.CharField(default="", max_length=100)),
                ("date", models.DateField(default="2024-01-01")),
                ("cureCost", models.IntegerField()),
                ("medicineCost", models.IntegerField()),
            ],
        ),
    ]
