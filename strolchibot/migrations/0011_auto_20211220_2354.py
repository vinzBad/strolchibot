# Generated by Django 3.2.8 on 2021-12-20 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strolchibot', '0010_auto_20211220_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='streamer',
            field=models.TextField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='config',
            name='link_protection_active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='config',
            name='link_protection_permit_subs',
            field=models.BooleanField(default=True, verbose_name='Permit Subs'),
        ),
    ]