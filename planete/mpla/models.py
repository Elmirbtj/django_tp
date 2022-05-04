from django.db import models
class Mpla(models.Model):
    titre = models.CharField(max_length=100)

    nom = models.CharField(max_length = 100)
    date_de_decouverte = models.DateField(blank=True, null = True)

    def __str__(self):
        chaine = f"{self.titre} {self.nom} a etait decouvert le{self.date_de_decouverte}"
        return chaine
    def dico(self):
        return {"titre" : self.titre, "nom" : self.nom, "date_parution" : self.date_de_decouverte }

class Pla(models.Model):
    titre = models.CharField(max_length=100)

    nom = models.CharField(max_length = 100)
    date_de_decouverte = models.DateField(blank=True, null = True)

    def __str__(self):
        chaine = f"{self.titre} ouho {self.nom} a etait decouvert le{self.date_de_decouverte}"
        return chaine
