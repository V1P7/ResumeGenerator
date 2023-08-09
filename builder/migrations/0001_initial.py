# Generated by Django 4.2.4 on 2023-08-09 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('city', models.CharField(max_length=100)),
                ('social', models.CharField(blank=True, max_length=100)),
                ('date_of_birth', models.DateField()),
                ('photo', models.ImageField(blank=True, upload_to='photos/')),
                ('education', models.CharField(max_length=150)),
                ('work_experience', models.CharField(max_length=150)),
                ('hard_skills', models.TextField()),
                ('soft_skills', models.TextField()),
                ('languages', models.CharField(max_length=100)),
                ('motivation_letter', models.TextField()),
            ],
        ),
    ]
