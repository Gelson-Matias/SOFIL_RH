# Generated by Django 2.2.1 on 2019-11-03 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core_help', '0016_estatistica_opcao'),
        ('secretaria', '0042_auto_20191027_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='nota_final_monografia',
            name='especialidade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, parent_link=True, to='core_help.Especialidade'),
        ),
    ]
