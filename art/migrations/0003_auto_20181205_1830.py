# Generated by Django 2.1.4 on 2018-12-05 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0002_auto_20181205_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='height',
        ),
        migrations.RemoveField(
            model_name='image',
            name='width',
        ),
    ]
