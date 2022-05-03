from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
class MplaForm(ModelForm):

    class Meta:
        model = models.Mpla
        fields = ('titre', 'nom', 'date_de_decouverte',)
        labels = {
            'titre' : _('Titre'),
            'nom' : _('Nom') ,
            'date_de_decouverte' : _('Date_de_decouverte'),


        }


class PlaForm(ModelForm):

    class Meta:
        model = models.Pla
        fields = ('titre', 'nom', 'date_de_decouverte',)
        labels = {
            'titre' : _('Titre'),
            'nom' : _('Nom') ,
            'date_de_decouverte' : _('Date_de_decouverte'),


        }