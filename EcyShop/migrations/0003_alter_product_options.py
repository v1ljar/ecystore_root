# Generated by Django 4.2.7 on 2023-11-29 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EcyShop', '0002_userdetails_alter_order_amount_of_items_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['title']},
        ),
    ]
