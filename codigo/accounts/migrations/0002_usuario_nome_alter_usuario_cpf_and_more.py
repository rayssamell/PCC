# Generated by Django 4.2 on 2023-05-24 00:25

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='nome',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cpf',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipoUsuario',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('P', 'Profissional'), ('F', 'Familiar')], max_length=12),
        ),
    ]