# Generated by Django 2.2.16 on 2020-11-01 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apppersona', '0002_persona_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='contraseña',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='contraseñaconfirmar',
        ),
    ]