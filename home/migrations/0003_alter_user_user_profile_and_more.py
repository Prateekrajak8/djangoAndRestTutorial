# Generated by Django 5.0.1 on 2024-01-10 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_user_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_profile',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_registration_date',
            field=models.DateField(null=True),
        ),
    ]
