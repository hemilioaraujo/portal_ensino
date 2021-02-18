# Generated by Django 3.1.6 on 2021-02-05 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aulas', '0002_popular_aula'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questao', models.TextField()),
                ('alt1', models.TextField()),
                ('alt2', models.TextField()),
                ('alt3', models.TextField()),
                ('alt4', models.TextField()),
                ('resposta_correta', models.TextField()),
                ('aula_referente', models.ForeignKey(
                    blank=True,
                    default=None,
                    null=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    to='aulas.aulas')),
            ],
            options={
                'verbose_name': 'Questão',
                'verbose_name_plural': 'Questões',
            },
        ),
    ]