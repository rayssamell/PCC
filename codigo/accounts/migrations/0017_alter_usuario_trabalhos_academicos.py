# Generated by Django 4.2 on 2023-08-01 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trabalhos_academicos', '0002_alter_trabalhos_academicos_ano_and_more'),
        ('accounts', '0016_auto_20230728_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='trabalhos_academicos',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='trabalhos_academicos.trabalhos_academicos'),
        ),
    ]
