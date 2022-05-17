from django.db import models

class Galaxie(models.Model):

    nom = models.CharField(max_length = 100)
    date_de_decouverte = models.CharField(max_length = 100,null=True)

    taille_s = models.CharField(max_length = 100 ,null=True)
    TYPE_CHOICES = [
        ("SP", 'Les galaxies spirales'),
        ("LEN" , 'Les galaxies lenticulaires '),
        ("ELL" , ' Les galaxies elliptiques '),
    ]

    type = models.CharField( max_length=40,
        choices=TYPE_CHOICES,
        default="SP",)
    image_galaxie = models.ImageField(upload_to="images")
    resume = models.TextField(null=True, blank=True)
    def __str__(self):
        return  self.nom

    def dico(self):
        return {"resume" :self.resume,"nom": self.nom, "date_de_decouverte": self.date_de_decouverte, "taille_s": self.taille_s, "type": self.type, "image_galaxie": self.image_galaxie}

class Pla(models.Model):

    galaxie = models.ForeignKey(Galaxie, on_delete=models.CASCADE, default=None, null=True)
    nom = models.CharField(max_length = 100)
    date_de_decouverte = models.CharField(max_length = 100 ,null=True)
    vitesse = models.CharField(max_length = 100 ,null=True)
    taille =models.CharField(max_length = 100 ,null=True)
    categorie = models.CharField(max_length = 100, )
    image_planete = models.ImageField(upload_to="images", null=True)
    resume = models.TextField(null=True, blank=True)
    def __str__(self):
        chaine = f"{self.nom} {self.date_de_decouverte}"
        return chaine
    def dico(self):
        return { "nom" : self.nom, "date_de_decouverte" : self.date_de_decouverte , "vitesse" :self.vitesse,"taille" :self.taille,"categorie" :self.categorie,
                 "resume": self.resume,"": self.galaxie, "": self.image_planete,
                 }





