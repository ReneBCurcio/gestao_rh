# Generated by Django 4.2.4 on 2023-08-09 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colaboradores', '0002_colaboradores_departamento_colaboradores_empresa_and_more'),
        ('documentos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentos',
            name='dono',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='colaboradores.colaboradores'),
        ),
    ]
