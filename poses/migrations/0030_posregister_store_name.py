# Generated by Django 3.2 on 2022-11-24 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poses', '0029_alter_posregister_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='posregister',
            name='store_name',
            field=models.CharField(default='خدماتیک', max_length=60, verbose_name='نام فروشگاه/شرکت'),
        ),
    ]
