# Generated by Django 4.2 on 2023-07-04 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_usuario_endereco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='endereco',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]