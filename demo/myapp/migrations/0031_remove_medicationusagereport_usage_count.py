# Generated by Django 5.0.3 on 2024-05-21 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0030_alter_medicationusagereport_usage_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicationusagereport',
            name='usage_count',
        ),
    ]
