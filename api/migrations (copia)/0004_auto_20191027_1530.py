# Generated by Django 2.2.6 on 2019-10-27 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20191027_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sombrilla',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='sombrilla',
            name='longitude',
            field=models.FloatField(),
        ),
    ]
