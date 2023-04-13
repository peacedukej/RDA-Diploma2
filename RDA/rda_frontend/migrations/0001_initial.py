# Generated by Django 3.2.18 on 2023-04-13 23:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('user_id', models.IntegerField(default=0)),
                ('analysis_id', models.AutoField(primary_key=True, serialize=False)),
                ('analysis_type', models.CharField(max_length=50, null=True)),
                ('date_of_upload_analysis', models.DateTimeField(null=True)),
                ('place_of_analysis', models.CharField(max_length=50, null=True)),
                ('analysis_user_name', models.CharField(max_length=50, null=True)),
                ('date_of_analysis', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease_id', models.IntegerField()),
                ('category', models.CharField(max_length=50, null=True)),
                ('disease_name', models.CharField(max_length=20, null=True)),
                ('ICD', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('doctor_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, null=True)),
                ('surname', models.CharField(max_length=30, null=True)),
                ('patronymic', models.CharField(max_length=30, null=True)),
                ('birthday', models.DateTimeField(null=True)),
                ('job', models.CharField(max_length=30, null=True)),
                ('start_of_experience', models.DateTimeField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('patronymic', models.CharField(max_length=30, null=True)),
                ('passport', models.CharField(max_length=20, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('birthday', models.DateTimeField(null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('address', models.CharField(max_length=50, null=True)),
                ('access_group', models.CharField(default='New', max_length=30, null=True)),
                ('photo', models.URLField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserDoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rda_frontend.doctor')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user_id', 'doctor_id')},
            },
        ),
        migrations.CreateModel(
            name='UserDisease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rda_frontend.disease')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user_id', 'disease_id')},
            },
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_id', models.IntegerField()),
                ('type', models.CharField(max_length=20, null=True)),
                ('link', models.CharField(max_length=100, null=True)),
                ('date_of_upload_file', models.DateTimeField(null=True)),
                ('file_user_name', models.CharField(max_length=20, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user_id', 'file_id')},
            },
        ),
    ]
