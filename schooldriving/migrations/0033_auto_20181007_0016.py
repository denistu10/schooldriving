# Generated by Django 2.1.1 on 2018-10-06 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schooldriving', '0032_branches_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branches',
            name='url',
            field=models.CharField(default='', help_text='gorelovo', max_length=250, verbose_name='Url страницы для записи'),
        ),
    ]
