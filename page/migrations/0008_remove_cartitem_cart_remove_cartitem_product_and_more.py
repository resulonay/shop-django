# Generated by Django 4.1.3 on 2023-01-09 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0007_cart_cartitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
