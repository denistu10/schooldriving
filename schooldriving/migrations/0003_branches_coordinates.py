# Generated by Django 2.1.1 on 2018-09-30 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schooldriving', '0002_tagline'),
    ]

    operations = [
        migrations.AddField(
            model_name='branches',
            name='coordinates',
            field=models.CharField(default='60.0520376,30.334460', help_text='Введите гео-координаты филиала вформате:60.0520376,30.334460.Взять в google', max_length=50, verbose_name='Координаты'),
        ),
    ]
