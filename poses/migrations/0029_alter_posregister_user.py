# Generated by Django 3.2 on 2022-11-24 07:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('poses', '0028_alter_posregister_businesslicense'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posregister',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='posregister', to=settings.AUTH_USER_MODEL, verbose_name='کارشناس فروش'),
        ),
    ]
