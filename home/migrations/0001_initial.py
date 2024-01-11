# Generated by Django 5.0.1 on 2024-01-03 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=255)),
                ('user_email', models.EmailField(max_length=255)),
                ('user_phone', models.CharField(max_length=255)),
                ('user_age', models.IntegerField()),
                ('user_profile', models.FileField(upload_to='')),
                ('user_registration_date', models.DateField()),
            ],
        ),
    ]
