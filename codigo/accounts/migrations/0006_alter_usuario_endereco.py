# Generated by Django 4.2 on 2023-07-04 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_usuario_descricao_alter_usuario_endereco_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='endereco',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
