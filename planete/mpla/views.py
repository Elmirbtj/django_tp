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
    liste2 = list(models.Pla.objects.filter(galaxie_id =id))
    return render(request,"mpla/affiche.html",{"galaxie": galaxie,'liste2' :liste2})



def traitementupdate(request, id):
    gform = GalaxieForm(request.POST, request.FILES)
    if gform.is_valid():
        galaxie = gform.save(commit=False)
        galaxie.id = id
        galaxie.save()
        return HttpResponseRedirect("/mpla/ajout")
    else:
        return render(request, "mpla/update.html", {"gform": gform, "id": id})


def update(request, id):
    galaxie = models.Galaxie.objects.get(pk=id)
    gform = GalaxieForm(galaxie.dico())
    return render(request, "mpla/update.html", {"gform": gform,"id":id})



def planete(request, id):
    if request.method == "POST":
        galaxie = models.Galaxie.objects.get(pk=id)
        form = PlaForm(request)
        if form.is_valid():
            planete = form.save(commit=False)
            planete.galaxie = galaxie
            planete.galaxie_id = id
            planete.save()

            return HttpResponseRedirect("/mpla/affiche")

        else:
            return render(request, "mpla/planete.html", {"form": form, "id": id})
    else :
        form = PlaForm()
        return render(request,"mpla/planete.html",{"form" : form,"id":id})



def traitement2(request, id):
    pform = PlaForm(request.POST, request.FILES)
    galaxie = models.Galaxie.objects.get(pk=id)
    if pform.is_valid():
        planete = pform.save(commit=False)
        planete.galaxie = galaxie
        planete.galaxie_id = id
        planete.save()
        return HttpResponseRedirect("/mpla/affiche/"+ str(id) )
    else:
        return render(request,"mpla/planete.html",{"pform": pform})

def delete2(request, id):

    pla = models.Pla.objects.get(pk=id)
    pla_id = pla.galaxie_id
    pla.delete()

    return HttpResponseRedirect(f"/mpla/affiche/{pla_id}")


def traitementupdate2(request, id):
    pform = PlaForm(request.POST, request.FILES)
    if pform.is_valid():
        pla=pform.save(commit=False)
        pla.id=id
        pla.save()
        return HttpResponseRedirect(f"/mpla/affiche")
    else:
        return render(request, "mpla/update2.html", {"pform": pform, "id": id})

def update2(request, id):
    pla = models.Pla.objects.get(pk=id)
    pform = PlaForm(pla.dico())
    return render(request, "mpla/update2.html", {"pform": pform,"id":id})


