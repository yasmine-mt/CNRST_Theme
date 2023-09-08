# Generated by Django 4.2.3 on 2023-09-05 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compte', '0006_remove_userprofile_is_gestionnaire'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('gestionnaire', 'Gestionnaire'), ('visiteur', 'Visiteur')], default='visiteur', max_length=20),
        ),
    ]