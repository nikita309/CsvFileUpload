# Generated by Django 4.0.3 on 2022-03-29 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CsvUpload', '0002_alter_uploadcsv_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadcsv',
            name='phone1_value',
            field=models.CharField(max_length=12),
        ),
    ]
