# Generated by Django 4.1.4 on 2023-02-04 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0010_alter_crypto_price6'),
    ]

    operations = [
        migrations.AddField(
            model_name='crypto',
            name='price10',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crypto',
            name='price7',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crypto',
            name='price8',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crypto',
            name='price9',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
