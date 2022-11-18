# Generated by Django 3.2 on 2022-11-18 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poses', '0017_alter_posregister_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posregister',
            name='back_nationalcard',
            field=models.FileField(upload_to='posdocuments/%Y/%m/%d/%S/', verbose_name='front national card'),
        ),
        migrations.AlterField(
            model_name='posregister',
            name='birthcertificate',
            field=models.FileField(upload_to='posdocuments/%Y/%m/%d/%S/', verbose_name='birth certificate'),
        ),
        migrations.AlterField(
            model_name='posregister',
            name='businesslicense',
            field=models.FileField(upload_to='posdocuments/%Y/%m/%d/%S/', verbose_name='businesslicense'),
        ),
        migrations.AlterField(
            model_name='posregister',
            name='front_nationalcard',
            field=models.FileField(upload_to='posdocuments/%Y/%m/%d/%S/', verbose_name='front national card'),
        ),
        migrations.AlterField(
            model_name='posregister',
            name='leaseterm',
            field=models.FileField(blank=True, upload_to='posdocuments/%Y/%m/%d/%S/', verbose_name='leaseterm'),
        ),
        migrations.AlterField(
            model_name='posregister',
            name='ownership_document',
            field=models.FileField(blank=True, upload_to='posdocuments/%Y/%m/%d/%S/', verbose_name='ownership document'),
        ),
        migrations.AlterField(
            model_name='posregister',
            name='sabin_form_first',
            field=models.FileField(upload_to='posdocuments/%Y/%m/%d/%S/', verbose_name='sabin form first'),
        ),
        migrations.AlterField(
            model_name='posregister',
            name='sabin_form_second',
            field=models.FileField(upload_to='posdocuments/%Y/%m/%d/%S/', verbose_name='sabin form second'),
        ),
        migrations.AlterField(
            model_name='posregister',
            name='signatureseal',
            field=models.FileField(upload_to='posdocuments/%Y/%m/%d/%S/', verbose_name='signature seal'),
        ),
        migrations.AlterField(
            model_name='posregister',
            name='user',
            field=models.ForeignKey(blank=True, default='Nov. 7, 2022, 10:15 a.m.', on_delete=django.db.models.deletion.CASCADE, related_name='posregisters', to='poses.user', to_field='national_code', verbose_name='parent'),
            preserve_default=False,
        ),
    ]