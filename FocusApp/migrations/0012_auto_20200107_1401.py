# Generated by Django 2.2.6 on 2020-01-07 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FocusApp', '0011_auto_20200102_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='have_data',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='table_name',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
