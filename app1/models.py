from django.db import models

# Create your models here.
class Beruf(models.Model):
    bezeichnung = models.CharField(("Bezeichnung"), max_length=250)
    kuerzel = models.CharField(("Kuerzel"), max_length=10, primary_key=True)
    def __str__(self):
        return self.kuerzel

class Lernfeldnr(models.Model):
    nummer = models.IntegerField(verbose_name=("Nummer:"), primary_key=True)
    bezeichnung = models.CharField(("Bezeichnung"), max_length=50)
    def __str__(self):
        return f"Lernfeld {self.nummer}"

class Ausbildungsjahr(models.Model):
    nummer = models.IntegerField(verbose_name=("Nummer:"), primary_key=True)
    bezeichnung = models.CharField(("Bezeichnung"), max_length=50)
    def __str__(self):
        return f"{self.nummer}. Lehrjahr"

class Vorlage(models.Model):
    quelle = models.CharField(("Quelle"), max_length=50, default="KMK-Beschluss vom")
    datum = models.DateField(("Beschluss"), auto_now=False, auto_now_add=False)
    def __str__(self):
        return f"{self.quelle} {self.datum}"

class Lernfeld(models.Model):
    beruf = models.ForeignKey(Beruf, verbose_name=("Beruf"), on_delete=models.CASCADE)
    lernfeldnr = models.ForeignKey(Lernfeldnr, verbose_name=("Lernfeldnummer"), on_delete=models.CASCADE)
    bezeichnung = models.TextField(("Bezeichnung"))
    kommentar = models.TextField(("zielformulierung"), blank=True)
    dauer = models.IntegerField(("Dauer (h)"))
    ausbildungsjahr = models.ForeignKey(Ausbildungsjahr, verbose_name=("Ausbildungsjahr"), on_delete=models.CASCADE)
    vorlage = models.ForeignKey(Vorlage, verbose_name=("Vorlage"), on_delete=models.CASCADE)
    def __str__(self):
        return f"LF {self.lernfeldnr.nummer} / {self.beruf} ({self.vorlage.datum})"

class Inhalt(models.Model):
    lernfeld = models.ForeignKey(Lernfeld, verbose_name=("Lernfeld"), on_delete=models.CASCADE)
    inhalt = models.TextField(("Inhalt"))
    kommentar = models.TextField(("Kommentar"), blank=True)
    def __str__(self):
        return f"{self.lernfeld} - {self.inhalt}" 


