# Generated by Django 3.2.5 on 2021-07-28 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='name',
        ),
    ]
