# Generated by Django 5.1.6 on 2025-04-09 18:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0016_remove_client_subscription'),
        ('creams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientrecords',
            name='cream',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='creams.creams'),
        ),
        migrations.AlterField(
            model_name='clientrecords',
            name='discount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='clientrecords',
            name='weight',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
