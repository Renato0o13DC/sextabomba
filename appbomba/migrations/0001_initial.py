# Generated by Django 4.2.2 on 2023-06-27 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarroBomba',
            fields=[
                ('patente', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=15)),
                ('nomenclatura', models.CharField(max_length=5)),
            ],
        ),
    ]
