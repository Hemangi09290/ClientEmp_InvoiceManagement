# Generated by Django 3.1.3 on 2021-03-18 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceapp', '0021_auto_20210318_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='cin',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='company_bank_add_text',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
