# Generated by Django 4.1.4 on 2023-01-28 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0007_crypto_price6'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crypto',
            name='price6',
            field=models.FloatField(blank=True, default=models.FloatField(blank=True, null=True), null=True),
        ),
    ]
