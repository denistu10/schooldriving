# Generated by Django 2.1.1 on 2018-09-30 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schooldriving', '0003_branches_coordinates'),
    ]

    operations = [
        migrations.AddField(
            model_name='tagline',
            name='end_phrase',
            field=models.CharField(default=None, max_length=300, verbose_name='Начало фразы на главной странице:'),
        ),
        migrations.AlterField(
            model_name='tagline',
            name='phrase',
            field=models.CharField(max_length=300, verbose_name='Начало фразы на главной странице:'),
        ),
    ]
