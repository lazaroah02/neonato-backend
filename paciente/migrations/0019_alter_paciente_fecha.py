# Generated by Django 3.2.20 on 2023-09-23 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0018_alter_paciente_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='fecha',
            field=models.DateTimeField(),
        ),
    ]
