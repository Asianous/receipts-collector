# Generated by Django 4.2.3 on 2023-07-26 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_receipt_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='date',
            field=models.DateField(),
        ),
    ]