# Generated by Django 2.2 on 2022-11-12 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_badge'),
    ]

    operations = [
        migrations.AddField(
            model_name='league',
            name='border_line',
            field=models.IntegerField(default=8),
        ),
    ]
