# Generated by Django 4.0.4 on 2023-02-28 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_customer_name_remove_shippingaddress_city_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='fistname',
            new_name='firstname',
        ),
    ]
