# Generated by Django 3.1.3 on 2021-03-16 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceapp', '0017_auto_20210316_0716'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='company_bank',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='invoiceapp.companybankdetail'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='company_bank_acc_text',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoice',
            name='company_bank_acc_type_text',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoice',
            name='company_bank_add_text',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoice',
            name='company_bank_ifsc_text',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
