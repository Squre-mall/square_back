# Generated by Django 3.0.3 on 2020-02-23 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cloth', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cloths',
            new_name='Cloth',
        ),
        migrations.RenameField(
            model_name='cloth',
            old_name='clothsImg',
            new_name='clothImg',
        ),
    ]
