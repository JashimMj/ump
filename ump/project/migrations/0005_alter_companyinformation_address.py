# Generated by Django 3.2.1 on 2021-05-05 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_rename_logo_companyinformation_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyinformation',
            name='Address',
            field=models.TextField(blank=True, null=True),
        ),
    ]