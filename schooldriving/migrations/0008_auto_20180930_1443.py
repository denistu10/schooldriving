# Generated by Django 2.1.1 on 2018-09-30 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schooldriving', '0007_auto_20180930_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tagline',
            name='image',
            field=models.ImageField(upload_to='slider/', verbose_name='Изображение'),
        ),
    ]
