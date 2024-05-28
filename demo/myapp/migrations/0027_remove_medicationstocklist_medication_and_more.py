# Generated by Django 5.0.3 on 2024-05-21 12:29

import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_medication_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicationstocklist',
            name='medication',
        ),
        migrations.RemoveField(
            model_name='medicalexamination',
            name='medicine',
        ),
        migrations.RemoveField(
            model_name='medicationusagereport',
            name='medication',
        ),
        migrations.DeleteModel(
            name='NewMedication',
        ),
        migrations.RemoveField(
            model_name='medicationstocklist',
            name='stock_quantity',
        ),
        migrations.AddField(
            model_name='medicationstocklist',
            name='medication_name',
            field=models.CharField(default=3, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medicationstocklist',
            name='quantity',
            field=models.IntegerField(default=2, validators=[django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medicationstocklist',
            name='unit',
            field=models.CharField(choices=[('vien', 'Viên'), ('chai', 'Chai')], default='vien', max_length=10),
        ),
        migrations.AddField(
            model_name='medicationusagereport',
            name='medication_name',
            field=models.CharField(default=4, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='medicationstocklist',
            name='date_added',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.DeleteModel(
            name='Medication',
        ),
    ]