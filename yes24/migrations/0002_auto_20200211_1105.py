# Generated by Django 3.0.3 on 2020-02-11 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yes24', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yes',
            name='title',
            field=models.CharField(max_length=250, verbose_name='title'),
        ),
    ]
