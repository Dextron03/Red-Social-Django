# Generated by Django 5.0.2 on 2024-02-25 03:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_network', '0005_alter_mysocialuser_profile_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mysocialuser',
            old_name='profile_picture',
            new_name='profileimg',
        ),
    ]
