# Generated by Django 4.2.3 on 2023-08-02 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0003_rename_advertisements_advertisement'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='advertisement',
            table='advertisements',
        ),
    ]
