# Generated by Django 3.2 on 2022-11-24 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poses', '0030_posregister_store_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posregister',
            name='store_name',
            field=models.CharField(max_length=60, verbose_name='نام فروشگاه/شرکت'),
        ),
    ]
