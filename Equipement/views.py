import csv
import io
from Equipement.filters import EquipementFiltre
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Equipement
from Laboratoire.models import Laboratoire
from django.contrib.auth.models import User
from .forms import EquipementForm
from Etablissement.models import Etablissement
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.


def v(request):
    equipements = Equipement.objects.all()
    marques_distinctes = [marque[0] for marque in Equipement.objects.values_list('Marque').distinct()]
    context = {
        'equipements': equipements,
        'marques_distinctes': marques_distinctes,
    }

    return render(request, 'Visiteur/equi.html', context)

@login_required(login_url='connexion')
def accueil(request):
    equipements = Equipement.objects.all()
    laboratoires= Laboratoire.objects.all()
    visiteurs =  User.objects.count()
    total_equipements = equipements.count()
    total_laboratoires= laboratoires.count()
    total_visiteurs = User.objects.count()
    derniers_equipements = equipements.order_by('-Date_Acquisition')[:3]
 

    context = {
        'total_equipements': total_equipements,
        'total_laboratoires': total_laboratoires,
        'equipements': equipements,
        'derniers_equipements': derniers_equipements,
        'visiteurs':visiteurs,
        'total_visiteurs': total_visiteurs,
    }
    return render(request, 'Equipement/dashboard.html', context)




@login_required(login_url='connexion')

def showEquipement(request):
    equipements = Equipement.objects.all()
    marques_distinctes = [marque[0] for marque in Equipement.objects.values_list('Marque').distinct()]
    context = {
        'equipements': equipements,
        'marques_distinctes': marques_distinctes,
    }

    return render(request, 'Equipement/xmateriel.html', context)


@login_required(login_url='connexion')
def map(request):
    return render(request,'Equipement/map.html')

@login_required(login_url='connexion')   
def import_csv(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        file_extension = csv_file.name.split('.')[-1]
        if file_extension.lower() != 'csv':
            messages.error(request, "L'extension du fichier n'est pas valide. Veuillez sélectionner un fichier CSV.")
            return render(request, 'Equipement/import_csv.html')

        try:
            with csv_file.open('rb') as f:
                decoded_file = f.read().decode('utf-8')
                csv_data = csv.reader(io.StringIO(decoded_file), delimiter=',')
                
                # Ignore the first line (header)
                next(csv_data)

                for row in csv_data:
                    reference = row[0]
                    etat = 'Installé' 
                    marque = row[2]
                    date_acquisition_str = row[3]  # Extract date as a string from CSV
                    date_acquisition = datetime.strptime(date_acquisition_str, '%d-%m-%Y').date()  # Convert to date
                    laboratoire_name = row[4]
                    localisation = row[5]
                    telephone = row[6]
                    email = row[7]
                    abrv = row[8]
                    etablissement_name = row[9]
                    adresse = row[10]
                    etablissement_telephone = row[11]
                    etablissement_email = row[12]
                    categorie = row[13]
                    
                
                    # Recherchez l'établissement correspondant dans la base de données
                    try:
                        etablissement = Etablissement.objects.get(Nom_Etab=etablissement_name)
                    except Etablissement.DoesNotExist:
                        # Si l'établissement n'existe pas, créez une nouvelle instance
                        etablissement = Etablissement(
                            Nom_Etab=etablissement_name,
                            Adresse=adresse,
                            telephone=etablissement_telephone,
                            email=etablissement_email,
                        )
                        etablissement.save()
                    # Recherchez laboratoire correspondant dans la base de données
                    laboratoire, created_lab = Laboratoire.objects.get_or_create(
                        Nom_Lab=laboratoire_name,
                        defaults={
                            'Localisation': localisation,
                            'Telephone': telephone,
                            'Email': email,
                            'Abrv': abrv,
                            'Etablissement':etablissement,
                        }
                    )
                    
                    

                    # Créez une instance d'Equipement et enregistrez-la dans la base de données
                    equipement = Equipement(
                        Reference=reference,
                        Etat=etat,
                        Date_Acquisition=date_acquisition,
                        Marque=marque,
                        Laboratoire=laboratoire,
                        Categorie=categorie,
                    )
                    equipement.save()

                messages.success(request, 'Importation CSV réussie.')
                return redirect('showEquipement')

        except Exception as e:
              messages.error(request, 'Une erreur s\'est produite lors de l\'importation du fichier CSV. Veuillez vérifier le format et l\'encodage du fichier.')
              messages.error(request, f'Erreur détaillée : {str(e)}')  # Ajoutez un message d'erreur détaillé avec str(e)
              return render(request, 'Equipement/import_csv.html')

    return render(request, 'Equipement/import_csv.html')

                
       

@login_required(login_url='connexion')
def ajouter_equipement(request):
    form = EquipementForm()
    if request.method == 'POST': 
        form=EquipementForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('showEquipement')
    context={'form':form}
    return render(request, 'Equipement/ajouter_equipement.html',context)

@login_required(login_url='connexion')
def supprimer_equipement(request,pk):
    equipement=Equipement.objects.get(Reference=pk)
    if request.method == 'POST':
        equipement.delete()
        return redirect('showEquipement')
    context ={'item':equipement}
    return render(request,'Equipement/supprimer_equipement.html',context)

@login_required(login_url='connexion')
def search_equipments(request):
    search_query = request.GET.get('Marque')  
    equipements = Equipement.objects.all()

    if search_query:
        equipement_filter = EquipementFiltre(request.GET, queryset=equipements)
        equipements = equipement_filter.qs
    return render(request, 'Equipement/rechercher.html', {'equipements': equipements})

def modifier_etat(request, equipement_id):
    equipement = Equipement.objects.get(id=equipement_id)

    if request.method == 'POST':
        nouvel_etat = request.POST['nouvel_etat']
        equipement.Etat = nouvel_etat
        equipement.save()
        return redirect('showEquipement')
    
    return render(request, 'Equipement/modifier_etat.html', {'equipement': equipement})