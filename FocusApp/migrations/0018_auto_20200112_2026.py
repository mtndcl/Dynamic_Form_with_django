# Generated by Django 2.2.6 on 2020-01-12 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FocusApp', '0017_auto_20200112_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectuser',
            name='project',
        ),
        migrations.AddField(
            model_name='projectuser',
            name='Project',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='FocusApp.Project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='table_name',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]