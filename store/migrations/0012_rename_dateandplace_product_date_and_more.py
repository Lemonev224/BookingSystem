# Generated by Django 4.0.4 on 2023-06-20 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_orderitem_quantity_product_dateandplace_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='DateAndPlace',
            new_name='Date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='digital',
        ),
    ]
