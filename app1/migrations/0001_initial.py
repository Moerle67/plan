# Generated by Django 4.1.7 on 2023-02-27 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ausbildungsjahr',
            fields=[
                ('nummer', models.IntegerField(primary_key=True, serialize=False, verbose_name='Nummer:')),
                ('bezeichnung', models.CharField(max_length=50, verbose_name='Bezeichnung')),
            ],
        ),
        migrations.CreateModel(
            name='Beruf',
            fields=[
                ('bezeichnung', models.CharField(max_length=250, verbose_name='Bezeichnung')),
                ('kuerzel', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Kuerzel')),
            ],
        ),
        migrations.CreateModel(
            name='Lernfeldnr',
            fields=[
                ('nummer', models.IntegerField(primary_key=True, serialize=False, verbose_name='Nummer:')),
                ('bezeichnung', models.CharField(max_length=50, verbose_name='Bezeichnung')),
            ],
        ),
        migrations.CreateModel(
            name='Vorlage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quelle', models.CharField(default='KMK-Beschluss vom', max_length=50, verbose_name='Quelle')),
                ('datum', models.DateField(verbose_name='Beschluss')),
            ],
        ),
        migrations.CreateModel(
            name='Lernfeld',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bezeichnung', models.TextField(verbose_name='Bezeichnung')),
                ('kommentar', models.TextField(blank=True, verbose_name='zielformulierung')),
                ('dauer', models.IntegerField(verbose_name='Dauer (h)')),
                ('ausbildungsjahr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.ausbildungsjahr', verbose_name='Ausbildungsjahr')),
                ('beruf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.beruf', verbose_name='Beruf')),
                ('lernfeldnr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.lernfeldnr', verbose_name='Lernfeldnummer')),
                ('vorlage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.vorlage', verbose_name='Vorlage')),
            ],
        ),
        migrations.CreateModel(
            name='Inhalt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inhalt', models.CharField(max_length=50, verbose_name='Inhalt')),
                ('kommentar', models.TextField(blank=True, verbose_name='Kommentar')),
                ('lernfeld', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.lernfeld', verbose_name='Lernfeld')),
            ],
        ),
    ]