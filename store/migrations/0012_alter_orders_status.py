# Generated by Django 4.0.4 on 2022-05-27 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_orders_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(default='Pending', max_length=10),
        ),
    ]
