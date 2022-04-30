from django.db import models
class Mpla(models.Model):
    titre = models.CharField(max_length=100)

    nom = models.CharField(max_length = 100)
    date_de_decouverte = models.DateField(blank=True, null = True)

    def __str__(self):
        chaine = f"{self.titre}␣écrit␣par␣{self.nom}␣édité␣le␣{self.date_de_decouverte}"
        return chaine
