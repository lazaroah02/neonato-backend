# Generated by Django 3.2.20 on 2023-09-22 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_customuser_verified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='verified',
        ),
    ]