# Generated by Django 5.0.3 on 2024-04-17 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0002_ride_delete_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
            ],
        ),
    ]