# Generated by Django 3.0.5 on 2021-02-28 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0002_auto_20210228_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='car_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='rent',
            name='rent_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]