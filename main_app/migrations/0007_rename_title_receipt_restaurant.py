# Generated by Django 4.2.3 on 2023-07-27 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_rename_restaurant_receipt_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receipt',
            old_name='title',
            new_name='restaurant',
        ),
    ]
