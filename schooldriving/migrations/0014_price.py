# Generated by Django 2.1.1 on 2018-09-30 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schooldriving', '0013_auto_20180930_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Название курса:')),
                ('price', models.CharField(max_length=500, verbose_name='Цена курса:')),
                ('image', models.ImageField(upload_to='price/', verbose_name='Изображение')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен:')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='Описание курса:')),
            ],
        ),
    ]
