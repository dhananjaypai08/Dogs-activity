# Generated by Django 4.0.5 on 2022-06-24 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0008_alter_dog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
