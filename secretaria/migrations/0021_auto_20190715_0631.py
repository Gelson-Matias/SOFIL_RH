# Generated by Django 2.2.1 on 2019-07-15 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretaria', '0020_auto_20190715_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudante',
            name='numero_estudante',
            field=models.CharField(blank=True, default=0, max_length=30),
        ),
    ]