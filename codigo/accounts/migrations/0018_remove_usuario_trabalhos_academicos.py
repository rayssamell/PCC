# Generated by Django 4.2 on 2023-08-01 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_alter_usuario_trabalhos_academicos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='trabalhos_academicos',
        ),
    ]
