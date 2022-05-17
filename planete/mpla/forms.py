from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from django import forms





class GalaxieForm(ModelForm):

    class Meta:
        model = models.Galaxie
        fields = ('nom', 'date_de_decouverte','image_galaxie','taille_s','type', "resume")
        labels = {
            'nom' : _('Nom') ,
            'date_de_decouverte' : _('Date de decouverte'),

            'taille_s': _('Taille de la galaxie(km)'),
            'type': _('Type de la galaxie'),
            'image_galaxie': '',
            'resume': _('resume'),
        }
        localized_fields = ('date_de_decouverte',)


class PlaForm(ModelForm):

    class Meta:
        model = models.Pla
        fields = ('nom', 'date_de_decouverte',  'image_planete', 'vitesse', 'taille', 'categorie',"resume")
        labels = {

            'nom' : _('Nom') ,
            'date_de_decouverte' : _('Date_de_decouverte'),

            'vitesse': _('Vitesse de rotation'),
            'taille': _('taille'),
            'categorie': _('categorie'),
            'image_planete': '',
            'resume': _('resume'),
        }