# Generated by Django 2.2 on 2022-02-28 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='recommend',
            field=models.ManyToManyField(blank=True, null=True, related_name='recommend', to='app.Song'),
        ),
    ]