# Generated by Django 4.0 on 2022-05-01 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_address_address_address_address1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='default',
            field=models.BooleanField(default=False, verbose_name='Default'),
        ),
    ]
