# Generated by Django 2.2.6 on 2020-01-12 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FocusApp', '0016_projectuser_is_accepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='fieldmondatory',
            field=models.BooleanField(default=False),
        ),
    ]
