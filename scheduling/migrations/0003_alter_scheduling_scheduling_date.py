# Generated by Django 4.0.6 on 2022-07-09 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling', '0002_alter_scheduling_scheduling_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduling',
            name='scheduling_date',
            field=models.DateField(),
        ),
    ]
