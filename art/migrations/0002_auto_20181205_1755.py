# Generated by Django 2.1.4 on 2018-12-05 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artproject',
            name='file',
            field=models.ImageField(blank=True, default='sources/no-img.jpg', null=True, upload_to='output/'),
        ),
    ]
