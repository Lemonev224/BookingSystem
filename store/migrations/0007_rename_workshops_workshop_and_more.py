# Generated by Django 4.0.4 on 2023-03-01 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_workshops_remove_orderitem_product_delete_product_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Workshops',
            new_name='Workshop',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='workshops',
            new_name='workshop',
        ),
    ]
