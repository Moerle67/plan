# Generated by Django 4.1.7 on 2023-02-27 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inhalt',
            name='inhalt',
            field=models.TextField(verbose_name='Inhalt'),
        ),
    ]
