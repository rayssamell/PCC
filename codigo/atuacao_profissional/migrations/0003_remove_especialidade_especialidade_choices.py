# Generated by Django 4.2 on 2023-05-21 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atuacao_profissional', '0002_alter_especialidade_especialidade_add'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='especialidade',
            name='especialidade_CHOICES',
        ),
    ]
