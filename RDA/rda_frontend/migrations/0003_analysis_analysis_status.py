# Generated by Django 3.2.18 on 2023-04-14 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rda_frontend', '0002_analysisfields'),
    ]

    operations = [
        migrations.AddField(
            model_name='analysis',
            name='analysis_status',
            field=models.CharField(default='Created', max_length=20),
        ),
    ]
