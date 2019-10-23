# Generated by Django 2.2.6 on 2019-10-20 15:58

import apps.bebidas.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tamanhoBebidas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bebida',
            fields=[
                ('idBebida', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(default='texto')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=4)),
                ('isAlcoolico', models.CharField(choices=[('yes', 'sim'), ('no', 'não')], max_length=5)),
                ('quantidade', models.DecimalField(decimal_places=4, default=0.0, max_digits=4)),
                ('foto', models.ImageField(default='sem-imagem-avatar.png', upload_to=apps.bebidas.models.user_directory_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('bebidaTamanhoBebida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tamanhoBebidas.tamanhoBebida')),
            ],
            options={
                'verbose_name': 'Bebida',
                'verbose_name_plural': 'Bebidas',
                'ordering': ['nome'],
            },
        ),
    ]
