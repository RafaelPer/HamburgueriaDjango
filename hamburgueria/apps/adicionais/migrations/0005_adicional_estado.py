# Generated by Django 2.2.6 on 2019-10-22 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adicionais', '0004_auto_20191021_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='adicional',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]
