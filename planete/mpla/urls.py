from django.urls import path

from . import views

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('home/', views.home),
    path('ajout/', views.ajout),
    path('traitement', views.traitement),
    path('/affiche/<int:id>/',views.affiche),
    path('/traitementupdate/<int:id>/',views.traitementupdate),




]