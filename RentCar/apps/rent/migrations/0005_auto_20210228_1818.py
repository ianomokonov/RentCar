# Generated by Django 3.0.5 on 2021-02-28 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0004_auto_20210228_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='rent_date',
            field=models.DateTimeField(blank=True, verbose_name='Дата бронирования'),
        ),
    ]