# Generated by Django 5.1.6 on 2025-04-09 17:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0014_clientrecords'),
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='subscription',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='subscriptions.subscription'),
        ),
    ]
