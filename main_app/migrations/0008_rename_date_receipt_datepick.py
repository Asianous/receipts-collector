# Generated by Django 4.2.3 on 2023-07-28 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_rename_title_receipt_restaurant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receipt',
            old_name='date',
            new_name='datepick',
        ),
    ]
