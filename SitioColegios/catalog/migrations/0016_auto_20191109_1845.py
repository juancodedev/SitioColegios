# Generated by Django 2.2.6 on 2019-11-09 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_remove_school_shortreview'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ratings',
            old_name='Rating',
            new_name='Score',
        ),
    ]
