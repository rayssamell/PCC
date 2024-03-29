# Generated by Django 4.2 on 2023-06-23 20:18

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('atuacao_profissional', '0003_remove_especialidade_especialidade_choices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atuacao_profissional',
            name='dias_atendimento',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('segunda', 'Segunda'), ('terça', 'Terça'), ('quarta', 'Quarta'), ('quinta', 'Quinta'), ('sexta', 'Sexta'), ('sabado', 'Sabado')], max_length=50),
        ),
    ]
