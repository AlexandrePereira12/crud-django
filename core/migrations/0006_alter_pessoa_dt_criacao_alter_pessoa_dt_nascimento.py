# Generated by Django 5.1.7 on 2025-03-18 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_pessoa_dt_criacao_pessoa_dt_nascimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='dt_criacao',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='dt_nascimento',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
