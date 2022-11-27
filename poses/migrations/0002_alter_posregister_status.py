# Generated by Django 3.2 on 2022-11-26 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posregister',
            name='status',
            field=models.CharField(blank=True, choices=[('ثبت درخواست ', 'ثبت درخواست'), ('مشاهده شد', 'مشاهده شد'), ('درحال بررسی', 'درحال بررسی'), ('رد درخواست (نامرتبط بودن صنف)', 'رد از طرف شرکت (نامرتبط بودن صنف)'), ('ثبت شاپرک', 'ثبت شاپرک'), ('رد به علت نقص مدارک', 'رد به علت نقص مدارک'), ('اختصاص ترمینال', 'اختصاص ترمینال'), ('نصب شد', 'نصب شد')], default='ثبت درخواست', max_length=60, verbose_name='وضعیت'),
        ),
    ]
