# Generated by Django 5.1 on 2024-08-14 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_alter_imagegallerymodel_dog_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagegallerymodel',
            name='dog_details',
            field=models.TextField(max_length=10000, null=True),
        ),
    ]