# Generated by Django 4.0.5 on 2022-07-20 15:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mushakta_baza', '0002_remove_tan_mshromeli_dab_tar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tan_mshromeli',
            name='Dab_Tar',
            field=models.DateField(default=datetime.datetime(2022, 7, 20, 19, 19, 7, 789940)),
        ),
        migrations.AlterField(
            model_name='tan_mshromeli',
            name='Piradi_Nom',
            field=models.CharField(max_length=11),
        ),
    ]