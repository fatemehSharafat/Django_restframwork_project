# Generated by Django 3.2 on 2022-11-24 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20221124_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='با فعال کردن این گزینه این کاربر میتواند به پنل مدیریت دسترسی داشته باشد', verbose_name='کاربر جمع آوری اطلاعات'),
        ),
    ]
