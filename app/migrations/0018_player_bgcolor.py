# Generated by Django 2.2 on 2022-04-09 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_songinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='bgColor',
            field=models.CharField(default='#ffffff', max_length=100),
        ),
    ]