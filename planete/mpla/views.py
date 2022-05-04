from django.shortcuts import render
from .forms import MplaForm
from .forms import PlaForm
from . import models
from django.http import HttpResponseRedirect

def ajout(request):
    if request.method == "POST":

        form = MplaForm(request)
        if form.is_valid():
            mpla = form.save()
            return render(request,"/mpla/affiche.html",{"mpla" : mpla})

        else:
            return render(request,"mpla/ajout.html",{"form": form})
    else :
        form = MplaForm()
        return render(request,"mpla/ajout.html",{"form" : form})

def delete(request, id):
    mpla = models.Mpla.objects.get(pk=id)
    mpla.delete()
    return HttpResponseRedirect("/mpla/home")

def Galaxie(request):
    liste = list(models.Mpla.objects.all())
    return render(request, 'mpla/Galaxie.html', {'liste': liste})


def planete(request):
    if request.method == "POST":

        form = PlaForm(request)
        if form.is_valid():
            pla = form.save()
            return render(request,"/mpla/affiche2.html",{"pla" : pla})

        else:
            return render(request,"mpla/planete.html",{"form": form})
    else :
        form = PlaForm()
        return render(request,"mpla/planete.html",{"form" : form})

def affiche2(request, id):
    pla = models.Pla.objects.get(pk=id)

    return render(request,"mpla/affiche2.html",{"pla": pla})

def traitement2(request):
    mform = PlaForm(request.POST)
    if mform.is_valid():
        pla = mform.save()
        return render(request,"mpla/affiche2.html",{"pla" : pla})
    else:
        return render(request,"mpla/planete.html",{"form": mform})

def delete2(request, id):
    pla = models.Pla.objects.get(pk=id)
    pla.delete()
    return HttpResponseRedirect("/mpla/affiche")


def traitementupdate2(request, id):
    mform = PlaForm(request.POST)
    if mform.is_valid():
        pla = lform.save(commit=False)

        pla.id = id ;
        pla.save()
        return HttpResponseRedirect("/mpla/planete")
    else:
        return render(request, "mpla/update.html", {"form": mform, "id": id})

def home(request):
    liste = list(models.Mpla.objects.all())
    return render(request, 'mpla/home.html', {'liste': liste})

def traitement(request):
    lform = MplaForm(request.POST)
    if lform.is_valid():
        mpla = lform.save()
        return HttpResponseRedirect("/mpla/home")
    else:
        return render(request,"mpla/ajout.html",{"form": lform})


def affiche(request, id):
    mpla = models.Mpla.objects.get(pk=id)

    return render(request,"mpla/affiche.html",{"mpla": mpla})



def traitementupdate(request, id):
    lform = MplaForm(request.POST)
    if lform.is_valid():
        mpla = lform.save(commit=False)

        mpla.id = id ;
        mpla.save()
        return HttpResponseRedirect("/mpla/ajout")
    else:
        return render(request, "mpla/update.html", {"form": lform, "id": id})


def update(request, id):
    mpla = models.Mpla.objects.get(pk=id)
    lform = MplaForm(mpla.dico())
    return render(request, "mpla/update.html", {"form": lform,"id":id})

