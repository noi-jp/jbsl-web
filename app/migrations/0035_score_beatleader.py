# Generated by Django 2.2 on 2022-11-27 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_auto_20221121_0312'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='beatleader',
            field=models.CharField(default='', max_length=100),
        ),
    ]
