# Generated by Django 2.2.6 on 2019-11-24 23:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0036_remove_school_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratings',
            name='Score',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Evaluacion de la escuela'),
        ),
    ]
