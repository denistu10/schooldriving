# Generated by Django 2.1.1 on 2018-09-30 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schooldriving', '0008_auto_20180930_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tagline',
            name='image',
            field=models.ImageField(height_field=1067, upload_to='slider/', verbose_name='Изображение', width_field=1920),
        ),
    ]
