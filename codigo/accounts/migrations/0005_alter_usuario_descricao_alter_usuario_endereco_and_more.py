# Generated by Django 4.2 on 2023-07-04 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formacao', '0001_initial'),
        ('forum', '0003_alter_mensagem_autor'),
        ('accounts', '0004_alter_usuario_tipousuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='descricao',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='endereco',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='formacao',
            field=models.ManyToManyField(null=True, to='formacao.formacao'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='sala',
            field=models.ManyToManyField(null=True, to='forum.sala'),
        ),
    ]
