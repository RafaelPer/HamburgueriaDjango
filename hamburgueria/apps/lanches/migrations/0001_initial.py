# Generated by Django 2.2.6 on 2019-10-20 15:58

import apps.lanches.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ingredientes', '0001_initial'),
        ('tamanhoLanche', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lanche',
            fields=[
                ('idLanche', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(default='')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=4)),
                ('foto', models.ImageField(default='sem-imagem-avatar.png', upload_to=apps.lanches.models.user_directory_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('lancheIngrediente', models.ManyToManyField(to='ingredientes.Ingrediente')),
                ('lancheTamanhoLanche', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tamanhoLanche.tamanhoLanche')),
            ],
            options={
                'verbose_name': 'Lanche',
                'verbose_name_plural': 'Lanches',
                'ordering': ['nome'],
            },
        ),
    ]
