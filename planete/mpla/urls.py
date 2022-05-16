from django.urls import path

from . import views

from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('home/', views.home),
    path('ajout/', views.ajout),
    path('traitement/', views.traitement),
    path('affiche/<int:id>/',views.affiche),
    path('traitementupdate/<int:id>',views.traitementupdate),
    path("delete/<int:id>", views.delete),
    path("update/<int:id>",views.update),
    path('planete/<int:id>', views.planete),
    path('traitement2/<int:id>', views.traitement2),
    path('traitementupdate2/<int:id>',views.traitementupdate2),
    path("delete2/<int:id>", views.delete2),
    path("update2/<int:id>",views.update2),



]

