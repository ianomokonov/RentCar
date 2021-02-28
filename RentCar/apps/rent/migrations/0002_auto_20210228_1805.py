# Generated by Django 3.0.5 on 2021-02-28 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='color',
            field=models.CharField(max_length=100, verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='release_year',
            field=models.IntegerField(verbose_name='Год выпуска'),
        ),
    ]