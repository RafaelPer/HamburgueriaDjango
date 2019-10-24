# Generated by Django 2.2.6 on 2019-10-23 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fornecedores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adicional',
            fields=[
                ('idAdicional', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(default='texto')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantidade', models.DecimalField(decimal_places=5, max_digits=10)),
                ('unidade', models.CharField(max_length=3)),
                ('isFalta', models.BooleanField(default=False)),
                ('estado', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('adicionalFornecedor', models.ManyToManyField(to='fornecedores.Fornecedor')),
            ],
            options={
                'verbose_name': 'Adicional',
                'verbose_name_plural': 'Adicionais',
                'ordering': ['nome'],
            },
        ),
    ]
