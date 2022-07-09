# Generated by Django 4.0.6 on 2022-07-09 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduling',
            name='scheduling_date',
            field=models.DateField(choices=[('09:00:00.00000', 'Novehoram'), ('10:00:00.00000', 'Dezhoram'), ('11:00:00.00000', 'Onzehoram'), ('12:00:00.00000', 'Dozehoram'), ('13:00:00.00000', 'Umahorat'), ('14:00:00.00000', 'Duashorast'), ('15:00:00.00000', 'Treshorast'), ('16:00:00.00000', 'Quatrohorast'), ('17:00:00.00000', 'Cincohorast'), ('18:00:00.00000', 'Seishorast'), ('19:00:00.00000', 'Setehorast'), ('20:00:00.00000', 'Oitohorast'), ('21:00:00.00000', 'Novehorast'), ('22:00:00.00000', 'Dezhorast')]),
        ),
        migrations.AlterField(
            model_name='scheduling',
            name='scheduling_end',
            field=models.TimeField(choices=[('09:00:00.00000', 'Novehoram'), ('10:00:00.00000', 'Dezhoram'), ('11:00:00.00000', 'Onzehoram'), ('12:00:00.00000', 'Dozehoram'), ('13:00:00.00000', 'Umahorat'), ('14:00:00.00000', 'Duashorast'), ('15:00:00.00000', 'Treshorast'), ('16:00:00.00000', 'Quatrohorast'), ('17:00:00.00000', 'Cincohorast'), ('18:00:00.00000', 'Seishorast'), ('19:00:00.00000', 'Setehorast'), ('20:00:00.00000', 'Oitohorast'), ('21:00:00.00000', 'Novehorast'), ('22:00:00.00000', 'Dezhorast')]),
        ),
        migrations.AlterField(
            model_name='scheduling',
            name='scheduling_start',
            field=models.TimeField(choices=[('09:00:00.00000', 'Novehoram'), ('10:00:00.00000', 'Dezhoram'), ('11:00:00.00000', 'Onzehoram'), ('12:00:00.00000', 'Dozehoram'), ('13:00:00.00000', 'Umahorat'), ('14:00:00.00000', 'Duashorast'), ('15:00:00.00000', 'Treshorast'), ('16:00:00.00000', 'Quatrohorast'), ('17:00:00.00000', 'Cincohorast'), ('18:00:00.00000', 'Seishorast'), ('19:00:00.00000', 'Setehorast'), ('20:00:00.00000', 'Oitohorast'), ('21:00:00.00000', 'Novehorast'), ('22:00:00.00000', 'Dezhorast')]),
        ),
    ]
