# Generated by Django 2.2.6 on 2021-06-04 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceapp', '0031_invoice_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='logo',
            field=models.ImageField(blank=True, default='client.png', null=True, upload_to='logo'),
        ),
    ]