# Generated by Django 4.2 on 2023-07-04 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_usuario_nome_alter_usuario_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='tipoUsuario',
            field=models.CharField(choices=[('P', 'Profissional'), ('F', 'Familiar')], default='P', max_length=1),
        ),
    ]
