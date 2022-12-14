# Generated by Django 3.1.3 on 2021-03-17 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceapp', '0017_auto_20210316_0716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='invoice_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='invoice_initial',
            field=models.CharField(default='SYS-INV', max_length=50),
        ),
    ]
