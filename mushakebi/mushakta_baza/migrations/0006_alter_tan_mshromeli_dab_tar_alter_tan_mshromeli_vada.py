# Generated by Django 4.0.5 on 2022-07-27 13:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mushakta_baza', '0005_alter_tan_mshromeli_dab_tar_alter_tan_mshromeli_vada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tan_mshromeli',
            name='Dab_Tar',
            field=models.DateField(default=datetime.datetime(2022, 7, 27, 17, 35, 31, 719004)),
        ),
        migrations.AlterField(
            model_name='tan_mshromeli',
            name='Vada',
            field=models.DateField(default=datetime.datetime(2022, 7, 27, 17, 35, 31, 719004)),
        ),
    ]
