# Generated by Django 3.0.3 on 2020-02-06 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20200206_0045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='comment',
        ),
    ]
