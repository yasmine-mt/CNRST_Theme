# Generated by Django 4.2.3 on 2023-09-05 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compte', '0002_remove_userprofile_is_superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
