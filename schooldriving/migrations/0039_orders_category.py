# Generated by Django 2.1.1 on 2018-10-07 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schooldriving', '0038_auto_20181007_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='schooldriving.Price'),
        ),
    ]
