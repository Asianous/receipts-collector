# Generated by Django 4.2.3 on 2023-07-27 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_receipt_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
