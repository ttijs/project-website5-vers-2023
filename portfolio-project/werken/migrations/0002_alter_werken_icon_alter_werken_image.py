# Generated by Django 4.2.6 on 2023-10-11 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('werken', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='werken',
            name='icon',
            field=models.ImageField(blank=True, upload_to='media/icon/'),
        ),
        migrations.AlterField(
            model_name='werken',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/images/'),
        ),
    ]