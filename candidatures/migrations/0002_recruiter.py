# Generated by Django 5.1.7 on 2025-03-21 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidatures', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('company', models.CharField(max_length=200)),
                ('job_title', models.CharField(max_length=100)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]
