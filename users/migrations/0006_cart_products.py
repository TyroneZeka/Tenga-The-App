# Generated by Django 4.0.3 on 2022-04-07 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_rename_img_url_media_image'),
        ('users', '0005_alter_customer_profilepicture'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Products.productmeta', verbose_name='Products in Cart'),
        ),
    ]
