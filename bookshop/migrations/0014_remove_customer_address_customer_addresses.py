# Generated by Django 4.2.4 on 2023-09-13 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop', '0013_remove_customer_address_customer_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='address',
        ),
        migrations.AddField(
            model_name='customer',
            name='addresses',
            field=models.ManyToManyField(blank=True, related_name='customer', to='bookshop.address'),
        ),
    ]
