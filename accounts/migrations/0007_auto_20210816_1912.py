# Generated by Django 3.2 on 2021-08-16 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210813_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='note',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
