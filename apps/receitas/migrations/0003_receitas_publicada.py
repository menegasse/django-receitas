# Generated by Django 3.1.7 on 2021-03-15 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0002_receitas_pessoa'),
    ]

    operations = [
        migrations.AddField(
            model_name='receitas',
            name='publicada',
            field=models.BooleanField(default=False),
        ),
    ]
