# Generated by Django 3.2 on 2021-04-21 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentarios',
            old_name='data',
            new_name='data_postagem',
        ),
    ]
