# Generated by Django 4.2 on 2023-04-30 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('universidade', models.CharField(max_length=150)),
                ('grau_academico', models.CharField(max_length=100)),
                ('especializacao', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
