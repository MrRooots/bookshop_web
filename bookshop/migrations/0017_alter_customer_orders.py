# Generated by Django 4.2.4 on 2023-09-20 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop', '0016_alter_customer_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='orders',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='bookshop.order'),
        ),
    ]