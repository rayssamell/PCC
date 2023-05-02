# Generated by Django 4.2 on 2023-04-30 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trabalhos_academicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_trabalho', models.CharField(max_length=150, verbose_name='Título do Trabalho')),
                ('autores', models.CharField(max_length=100, verbose_name='Autor(es)')),
                ('revista', models.CharField(max_length=50)),
                ('ano', models.DateField(verbose_name='Ano de Publicação')),
                ('anexo', models.FileField(default='', upload_to='meusarquivos/')),
            ],
        ),
    ]
