# Generated by Django 4.1.7 on 2023-03-23 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_customuser_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='last_name',
        ),
    ]
