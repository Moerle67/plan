from django.db import models

# Create your models here.
class Lernfeld(models.Model):
    

class Inhalte(models.Model):
    beruf = models.ForeignKey(Beruf, verbose_name=("Beruf"), on_delete=models.CASCADE)
    vorlage = models.ForeignKey(Vorlage, verbose_name=("Vorlage"), on_delete=models.CASCADE)
    lernfeld = models.ForeignKey(Lernfeld, verbose_name=("Lernfeld"), on_delete=models.CASCADE)
    inhalt = models.CharField(("Inhalt"), max_length=50)
    kommentar = models.TextField(("Kommentar"))

