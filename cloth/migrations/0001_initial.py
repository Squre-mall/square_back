# Generated by Django 3.0.3 on 2020-02-23 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cloths',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=100)),
                ('clothsImg', models.ImageField(upload_to='')),
                ('price', models.CharField(max_length=100)),
                ('category', models.IntegerField()),
            ],
        ),
    ]
