# Generated by Django 5.1.7 on 2025-03-18 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_name_pessoa_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='dt_criacao',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='dt_nascimento',
            field=models.DateField(blank=True, null=True),
        ),
    ]
