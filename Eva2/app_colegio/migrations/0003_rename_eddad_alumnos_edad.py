# Generated by Django 4.1.3 on 2022-11-18 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_colegio', '0002_rename_contacto_alumnos_eddad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumnos',
            old_name='eddad',
            new_name='edad',
        ),
    ]
