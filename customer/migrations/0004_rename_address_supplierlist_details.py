# Generated by Django 4.0.3 on 2022-04-11 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_alter_orders_number_alter_orders_quantity_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplierlist',
            old_name='address',
            new_name='details',
        ),
    ]
