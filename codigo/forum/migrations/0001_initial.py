# Generated by Django 4.2 on 2023-05-21 22:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', models.TextField()),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('anexo', models.ImageField(blank=True, upload_to='forum')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Mensagem',
            },
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('imagem', models.ImageField(blank=True, upload_to='forum')),
                ('mensagens', models.ManyToManyField(blank=True, null=True, to='forum.mensagem')),
            ],
            options={
                'verbose_name_plural': 'Salas',
            },
        ),
    ]
