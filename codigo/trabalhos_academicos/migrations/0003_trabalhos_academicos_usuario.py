# Generated by Django 4.2 on 2023-08-01 22:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trabalhos_academicos', '0002_alter_trabalhos_academicos_ano_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabalhos_academicos',
            name='usuario',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, related_name='trabalhos_academicos', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
