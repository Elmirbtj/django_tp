from django.db import models

class Galaxie(models.Model):

    nom = models.CharField(max_length = 100)
    date_de_decouverte = models.DateField(blank=True, null = True)

    distance = models.CharField(max_length = 100)
    taille_s = models.CharField(max_length=100, null = True)
    type = models.CharField(max_length=100, null = True)
    image_galaxie = models.ImageField(upload_to="images")
    def __str__(self):
        return  self.nom
    def dico(self):
        return { "nom" : self.nom, "date_parution" : self.date_de_decouverte,"distance": self.distance,"taille s": self.taille_s, "Type de la galaxie": self.type, "": self.image_galaxie,}

class Pla(models.Model):

    galaxie = models.ForeignKey(Galaxie, on_delete=models.CASCADE, default=None, null=True)

    nom = models.CharField(max_length = 100)
    date_de_decouverte = models.DateField(blank=True, null = True)

    vitesse = models.CharField(max_length = 100, null = True)
    taille = models.CharField(max_length = 100,null = True)
    categorie = models.CharField(max_length = 100, )
    image_planete = models.ImageField(upload_to="images", null=True)
    def __str__(self):
        chaine = f"{self.titre}{self.nom} {self.date_de_decouverte}"
        return chaine
    def dico(self):
        return { "nom" : self.nom, "date_parution" : self.date_de_decouverte }





