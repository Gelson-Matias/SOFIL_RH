# Generated by Django 2.2.1 on 2019-07-10 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('secretaria', '0011_auto_20190709_0545'),
        ('utilizador', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='controla_senhapadrao',
            name='pessoa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='secretaria.Pessoa'),
            preserve_default=False,
        ),
    ]
