# Generated by Django 2.2.6 on 2019-10-20 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tamanhoBebida',
            fields=[
                ('idTamanhoBebida', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'tamanhoBebida',
                'verbose_name_plural': 'tamanhosBebidas',
                'ordering': ['nome'],
            },
        ),
    ]
