# Generated by Django 5.1 on 2024-08-14 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='imageGallerymodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(null=True, upload_to='Media/dog_img')),
                ('dog_type', models.CharField(max_length=100)),
                ('dog_name', models.CharField(max_length=100)),
                ('dog_age', models.PositiveIntegerField()),
            ],
        ),
    ]
