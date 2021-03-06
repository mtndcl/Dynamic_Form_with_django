# Generated by Django 2.2.6 on 2019-12-08 19:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FocusApp', '0006_auto_20191208_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectuser',
            name='project',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='FocusApp.Project'),
        ),
        migrations.AlterField(
            model_name='projectuser',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
