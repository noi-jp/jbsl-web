# Generated by Django 2.2 on 2022-11-20 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_participant_decorate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='valid_acc',
            new_name='count_acc',
        ),
        migrations.RenameField(
            model_name='participant',
            old_name='pos',
            new_name='count_pos',
        ),
        migrations.RenameField(
            model_name='participant',
            old_name='weight_acc',
            new_name='count_weight_acc',
        ),
    ]