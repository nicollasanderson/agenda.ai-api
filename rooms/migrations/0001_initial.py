# Generated by Django 4.0.6 on 2022-07-09 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('LB', 'Laboratório'), ('SA', 'Sala de Aula')], default='SA', max_length=50)),
                ('block', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]