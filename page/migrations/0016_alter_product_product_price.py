# Generated by Django 4.1.3 on 2023-01-11 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0015_alter_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.CharField(max_length=500),
        ),
    ]
