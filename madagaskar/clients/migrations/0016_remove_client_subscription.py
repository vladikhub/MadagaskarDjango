# Generated by Django 5.1.6 on 2025-04-09 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0015_alter_client_subscription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='subscription',
        ),
    ]
