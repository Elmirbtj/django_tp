from django.shortcuts import render
from .forms import GalaxieForm
from .forms import PlaForm
from . import models
from django.http import HttpResponseRedirect



def ajout(request):
    if request.method == "POST":

        form = GalaxieForm(request)
        if form.is_valid():
            galaxie = form.save()
            return render(request,"/mpla/affiche.html",{"galaxie" : galaxie})

        else:
            return render(request,"mpla/ajout.html",{"form": form})
    else :
        form = GalaxieForm()
        return render(request,"mpla/ajout.html",{"form" : form})



def delete(request, id):
    galaxie = models.Galaxie.objects.get(pk=id)
    galaxie.delete()
    return HttpResponseRedirect("/mpla/home")

def Galaxie(request):
    liste = list(models.Galaxie.objects.all())
    return render(request, 'mpla/Galaxie.html', {'liste': liste})

def home(request):
    liste = list(models.Galaxie.objects.all())

    return render(request, 'mpla/home.html', {'liste': liste,})

def traitement(request):
    form = GalaxieForm(request.POST, request.FILES)
    if form.is_valid():
        galaxie = form.save()
        return HttpResponseRedirect("/mpla/home")
    else:
        return render(request,"mpla/ajout.html",{"form": form})


def affiche(request, id):
    galaxie = models.Galaxie.objects.get(pk=id)
    liste2 = list(models.Pla.objects.filter(galaxie_id = id))
    return render(request,"mpla/affiche.html",{"galaxie": galaxie,'liste2' :liste2})



def traitementupdate(request, id):
    gform = GalaxieForm(request.POST, request.FILES)
    if gform.is_valid():
        galaxie = gform.save(commit=False)
        galaxie.id = id
        galaxie.save()
        return HttpResponseRedirect("/mpla/ajout")
    else:
        return render(request, "mpla/update.html", {"form": gform, "id": id})


def update(request, id):
    galaxie = models.Galaxie.objects.get(pk=id)
    gform = GalaxieForm(galaxie.dico())
    return render(request, "mpla/update.html", {"form": gform,"id":id})



def planete(request):
    if request.method == "POST":
        galaxie = models.Galaxie.objects.get(pk=id)
        form = PlaForm(request)
        if form.is_valid():
            planete = pform.save(commit=False)
            planete.Galaxie = galaxie
            planete.Galaxie_id = id
            planete.save()
            return render(request,"/mpla/affiche.html",{"planete" : planete})

        else:
            return render(request,"mpla/planete.html",{"form": form})
    else :
        form = PlaForm()
        return render(request,"mpla/planete.html",{"form" : form})

def affiche2(request, id):
    galaxie = models.Galaxie.objects.get(pk=id)
    liste2 = list(models.Pla.objects.filter(galaxie_id = id))
    return render(request,"mpla/home.html",{"galaxie": galaxie,'liste2' :liste2})


def traitement2(request, id):
    pform = PlaForm(request.POST, request.FILES)
    galaxie = models.Galaxie.objects.get(pk=id)
    if pform.is_valid():
        planete = pform.save(commit=False)
        planete.Galaxie = galaxie
        planete.Galaxie_id = id
        planete.save()
        return HttpResponseRedirect("/mpla/affiche",{"id":id})
    else:
        return render(request,"mpla/planete.html",{"form": pform})

def delete2(request, id):
    pla = models.Pla.objects.get(pk=id)
    pla.delete()
    return HttpResponseRedirect(f"/mpla/affiche/{pla.galaxie_id}")


def traitementupdate2(request, id):
    pform = PlaForm(request.POST, request.FILES)
    if pform.is_valid():
        pla = mform.save(commit=False)

        pla.id = id
        pla.save()
        return HttpResponseRedirect("/mpla/planete")
    else:
        return render(request, "mpla/update.html", {"pform": pform, "id": id})

def update2(request, id):
    pla = models.Pla.objects.get(pk=id)
    pform = PlaForm(pla.dico())
    return render(request, "mpla/update2.html", {"form": pform,"id":id})


