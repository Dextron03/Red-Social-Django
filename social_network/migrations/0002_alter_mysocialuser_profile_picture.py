# Generated by Django 5.0.2 on 2024-02-23 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_network', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mysocialuser',
            name='profile_picture',
            field=models.ImageField(blank=True, default='profile_picture.jpeg', null=True, upload_to='media/profile/'),
        ),
    ]
