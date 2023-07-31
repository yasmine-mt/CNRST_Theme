from django.shortcuts import render

# Create your views here.


def accueil_visiteur(request):
    return render(request, 'Visiteur/accueil_visiteur.html')