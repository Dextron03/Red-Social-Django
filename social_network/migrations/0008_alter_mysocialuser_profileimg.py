# Generated by Django 5.0.2 on 2024-02-25 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_network', '0007_alter_mysocialuser_profileimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mysocialuser',
            name='profileimg',
            field=models.ImageField(blank=True, default='profile_picture.jpeg', null=True, upload_to='profiles/'),
        ),
    ]
