# Generated by Django 3.2.3 on 2022-04-14 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posApp', '0005_products_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesitems',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
