# Generated by Django 4.2.3 on 2023-09-05 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compte', '0004_userprofile_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='role',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_gestionnaire',
            field=models.BooleanField(default=False),
        ),
    ]
