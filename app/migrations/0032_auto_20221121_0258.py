# Generated by Django 2.2 on 2022-11-20 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_auto_20221120_0729'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='pos',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='participant',
            name='rank',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='participant',
            name='theoretical',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='participant',
            name='tooltip_acc',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='participant',
            name='tooltip_pos',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='participant',
            name='tooltip_valid',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='participant',
            name='tooltip_weight_acc',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='participant',
            name='valid_acc',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='participant',
            name='valid_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='participant',
            name='weight_acc',
            field=models.IntegerField(default=0),
        ),
    ]
