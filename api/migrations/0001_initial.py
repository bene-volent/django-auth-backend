# Generated by Django 5.1.3 on 2024-11-25 03:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(db_default=None, max_length=30)),
                ('username', models.CharField(db_index=True, max_length=256, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('hashed_password', models.CharField(max_length=72)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('task', models.CharField(max_length=100)),
                ('completed', models.BooleanField(default=False)),
                ('type', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='api.user')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]