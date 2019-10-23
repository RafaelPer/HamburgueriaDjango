# Generated by Django 2.2.6 on 2019-10-20 15:58

import apps.clientes.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cidade', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('idCliente', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(max_length=100)),
                ('rg', models.CharField(max_length=10)),
                ('cpf', models.CharField(max_length=12)),
                ('rua', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=9)),
                ('email', models.EmailField(max_length=100)),
                ('numeroCasa', models.CharField(max_length=6)),
                ('telefone1', models.CharField(max_length=24)),
                ('telefone2', models.CharField(max_length=24)),
                ('celular1', models.CharField(max_length=24)),
                ('celular2', models.CharField(max_length=24)),
                ('foto', models.ImageField(default='sem-imagem-avatar.png', upload_to=apps.clientes.models.user_directory_path)),
                ('ativo', models.CharField(choices=[('yes', 'sim'), ('no', 'não')], max_length=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('clienteCidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cidade.Cidade')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['nome'],
            },
        ),
    ]
