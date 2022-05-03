from django.shortcuts import render
from .forms import MplaForm
from .forms import PlaForm
from . import models
from django.http import HttpResponse

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

def home(request):
    return render(request, 'mpla/home.html')

def traitement(request):
    lform = MplaForm(request.POST)
    if lform.is_valid():
        mpla = lform.save()
        return render(request,"mpla/affiche.html",{"mpla" : mpla})
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
        return HttpResponseRedirect("/mpla")
    else:
        return render(request, "mpla/update.html", {"form": lform, "id": id})

