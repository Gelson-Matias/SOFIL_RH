# Generated by Django 2.2.1 on 2019-12-12 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretaria', '0050_auto_20191209_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='data_nascimento',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]