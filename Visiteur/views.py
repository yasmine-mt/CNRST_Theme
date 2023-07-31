from django.shortcuts import render,get_object_or_404
from .forms import ContactForm
from Equipement.models import Equipement
from Equipement.filters import EquipementFiltre
from django.contrib.auth.decorators import login_required
from Equipement.models import Laboratoire
# Create your views here.


def accueil_visiteur(request):
    return render(request, 'Visiteur/accueil_visiteur.html')




def search_equipments2(request):
    search_query = request.GET.get('Marque')  
    equipements = Equipement.objects.all()

    if search_query:
        equipement_filter = EquipementFiltre(request.GET, queryset=equipements)
        equipements = equipement_filter.qs
    return render(request, 'visiteur/rechercher2.html', {'equipements': equipements})


@login_required(login_url='connexion')

def contact_laboratoire(request, laboratoire_id):
    # Récupérer le laboratoire associé à l'équipement en utilisant laboratoire_id
    laboratoire = get_object_or_404(Laboratoire, id=laboratoire_id)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Traiter le formulaire et envoyer le message au laboratoire
            # Vous pouvez accéder aux champs du formulaire via form.cleaned_data
            nom = form.cleaned_data['nom']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Code pour envoyer le message au laboratoire (à personnaliser selon vos besoins)
            # ...

            # Rediriger l'utilisateur vers une page de confirmation ou une autre vue
            return render(request, 'visiteur/confirmation.html')
    else:
        # Vérifier si l'utilisateur est connecté (authentifié)
        if request.user.is_authenticated:
            # Si l'utilisateur est connecté, pré-remplir les champs nom et e-mail avec ses informations
            form = ContactForm(initial={'nom': request.user.get_full_name(), 'email': request.user.email})
        else:
            # Si l'utilisateur n'est pas connecté, laissez les champs nom et e-mail vides
            form = ContactForm()

    context = {
        'laboratoire': laboratoire,  # Passez ici le laboratoire associé à l'équipement
        'form': form,
    }

    return render(request, 'visiteur/contacter_labo.html', context)