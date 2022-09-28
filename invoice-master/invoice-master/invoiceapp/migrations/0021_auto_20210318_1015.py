# Generated by Django 3.1.3 on 2021-03-18 10:15

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceapp', '0020_merge_20210317_0920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='city',
        ),
        migrations.RemoveField(
            model_name='address',
            name='country',
        ),
        migrations.RemoveField(
            model_name='address',
            name='email_id',
        ),
        migrations.RemoveField(
            model_name='address',
            name='phone_no',
        ),
        migrations.RemoveField(
            model_name='address',
            name='state',
        ),
        migrations.AddField(
            model_name='address',
            name='address',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='email_id',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='phone_no',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='email_id',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='phone_no',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='companybankdetail',
            name='bank_address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='companybankdetail',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='bank_ad_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='bank_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='company_iec',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='company_lut_bond',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='company_pan_no',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='company_self_declaration',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='company_terms_condition',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='company_bank_add_text',
            field=models.CharField(max_length=300),
        ),
    ]
