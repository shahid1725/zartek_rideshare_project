# Generated by Django 5.0.3 on 2024-04-17 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0003_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ride',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='ride',
            name='updated_at',
        ),
    ]