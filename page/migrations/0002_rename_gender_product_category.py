# Generated by Django 4.1.3 on 2023-01-01 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='gender',
            new_name='category',
        ),
    ]
