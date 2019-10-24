# Generated by Django 2.2.6 on 2019-10-23 20:24

import apps.funcionarios.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tipoFuncionario', '0001_initial'),
        ('estado', '0001_initial'),
        ('pais', '0001_initial'),
        ('cidade', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('idFuncionario', models.AutoField(primary_key=True, serialize=False)),
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
                ('foto', models.ImageField(default='sem-imagem-avatar.png', upload_to=apps.funcionarios.models.user_directory_path)),
                ('ativo', models.CharField(choices=[('yes', 'sim'), ('no', 'não')], max_length=5)),
                ('senha', models.CharField(default='', max_length=50)),
                ('data_admissao', models.DateTimeField(default=datetime.datetime.now)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('funcionarioCidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cidade.Cidade')),
                ('funcionarioEstado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estado.Estado')),
                ('funcionarioPais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pais.Pais')),
                ('funcionarioTipoFuncionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tipoFuncionario.tipoFuncionario')),
            ],
            options={
                'verbose_name': 'Funcionario',
                'verbose_name_plural': 'Funcionarios',
                'ordering': ['nome'],
            },
        ),
    ]
