# Generated by Django 4.2.7 on 2023-11-02 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='codigo_de_barras',
            field=models.CharField(default='0', max_length=20, unique=True),
        ),
    ]