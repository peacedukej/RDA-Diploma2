# Generated by Django 3.2.18 on 2023-04-15 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rda_frontend', '0009_alter_analysisfields_value_30'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysisfields',
            name='value_30',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
