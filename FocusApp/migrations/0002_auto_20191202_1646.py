# Generated by Django 2.2.6 on 2019-12-02 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FocusApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='bio',
            new_name='organization',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='location',
            new_name='phone_number',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='birth_date',
        ),
    ]
