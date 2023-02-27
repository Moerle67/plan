from django.db import models

# Create your models here.
class Beruf(models.Model):
    bezeichnung = models.CharField(("Bezeichnung"), max_length=250)
    kuerzel = models.CharField(("Kuerzel"), max_length=10, primary_key=True)

class Lernfeldnr(models.Model):
    lernfeld = models.IntegerField(verbose_name=("Nummer:"), primary_key=True)
    bezeichnung = models.CharField(("Bezeichnung"), max_length=50)

class Ausbildungsjahr(models.Model):
    lernfeld = models.IntegerField(verbose_name=("Nummer:"), primary_key=True)
    bezeichnung = models.CharField(("Bezeichnung"), max_length=50)


class Vorlage(models.Model):
    quelle = models.CharField(("Quelle"), max_length=50, default="KMK-Beschluss vom")
    datum = models.DateField(("Beschluss"), auto_now=False, auto_now_add=False)

class Lernfeld(models.Model):
    beruf = models.ForeignKey(Beruf, verbose_name=("Beruf"), on_delete=models.CASCADE)
    lernfeldnr = models.ForeignKey(Lernfeldnr, verbose_name=("Lernfeldnummer"), on_delete=models.CASCADE)
    bezeichnung = models.models.TextField(("Bezeichnung"))
    kommentar = models.models.TextField(("zielformulierung"), empty=True)
    dauer = models.IntegerField(("Dauer (h)"))
    ausbildungsjahr = models.ForeignKey(Ausbildungsjahr, verbose_name=("Ausbildungsjahr"), on_delete=models.CASCADE)

class Inhalte(models.Model):
    vorlage = models.ForeignKey(Vorlage, verbose_name=("Vorlage"), on_delete=models.CASCADE)
    lernfeld = models.ForeignKey(Lernfeld, verbose_name=("Lernfeld"), on_delete=models.CASCADE)
    inhalt = models.CharField(("Inhalt"), max_length=50)
    kommentar = models.TextField(("Kommentar"), empty=True)

