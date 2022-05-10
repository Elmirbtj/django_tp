from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from django import forms





class GalaxieForm(ModelForm):

    class Meta:
        model = models.Galaxie
        fields = ('nom', 'date_de_decouverte','image_galaxie', 'distance','taille_s','type',)
        labels = {
            'nom' : _('Nom') ,
            'date_de_decouverte' : _('Date de decouverte'),

            'distance': _('Distance en fonction du systéme solaire'),
            'taile_s': _('Taille de la galaxie'),
            'type': _('Type de la galaxie'),
            'image_galaxie': '',
        }
        localized_fields = ('date_de_decouverte',)


class PlaForm(ModelForm):

    class Meta:
        model = models.Pla
        fields = ('nom', 'date_de_decouverte',  'image_planete', 'vitesse', 'taille', 'categorie',)
        labels = {

            'nom' : _('Nom') ,
            'date_de_decouverte' : _('Date_de_decouverte'),

            'vitesse': _('Vitesse de rotation'),
            'taille': _('taille'),
            'categorie': _('categorie'),
            'image_planete': '',
        }