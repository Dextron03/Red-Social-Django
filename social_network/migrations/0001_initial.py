# Generated by Django 5.0.2 on 2024-02-23 03:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MySocialUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='correo electronico')),
                ('username', models.CharField(max_length=70, unique=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=50)),
                ('surnames', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('profile_picture', models.ImageField(default='profile_picture.jpeg', upload_to='media/profile/')),
                ('activation_token', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_posts', models.TextField(max_length=400, verbose_name='Contenido')),
                ('img', models.ImageField(blank=True, upload_to='img_posts/')),
                ('hour', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='social_network.posts')),
            ],
        ),
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stablished_at', models.DateTimeField(auto_now_add=True)),
                ('friend', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='friends_of', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='friends', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'friend')},
            },
        ),
    ]