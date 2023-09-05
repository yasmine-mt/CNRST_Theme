from django.shortcuts import render,get_object_or_404,redirect
from .forms import ContactForm
from django.core.mail import send_mail
from Equipement.models import Equipement
from django.contrib.auth import logout
from Equipement.filters import EquipementFiltre
from django.contrib.auth.decorators import login_required
from .models import MessageReservation
from django.http import JsonResponse,HttpResponse
from django.views.decorators.http import require_POST
from django.conf import settings
import smtplib
from smtplib import SMTPException
from socket import gaierror
# Create your views here.


def accueil_visiteur(request):
    equipements = Equipement.objects.all()
    marques_distinctes = [marque[0] for marque in Equipement.objects.values_list('Marque').distinct()]
    context = {
        'equipements': equipements,
        'marques_distinctes': marques_distinctes,
    }

    return render(request, 'Visiteur/equi.html', context)



@login_required(login_url='connexion')
def my_account(request):
    user = request.user
    reservation_count = MessageReservation.objects.filter(nom=user.get_full_name()).count()
    context = {
        'user': user,
        'reservation_count': reservation_count,
    }
    return render(request, 'visiteur/mon_compte.html', context)


@login_required(login_url='connexion')
def delete_account(request):
    if request.method == 'POST':
        request.user.delete()
        logout(request)
        return redirect('accueil_visiteur')  
    return render(request, 'delete_account.html')


def search_equipments2(request):
    search_query = request.GET.get('Marque')  
    equipements = Equipement.objects.all()
    if search_query:
        equipement_filter = EquipementFiltre(request.GET, queryset=equipements)
        equipements = equipement_filter.qs
    return render(request, 'visiteur/rechercher2.html', {'equipements': equipements})


@login_required(login_url='connexion')

def contact_laboratoire(request, equipement_id):  
    equipement = get_object_or_404(Equipement, id=equipement_id)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            reservation_message = f"Bonjour,\n\nJe souhaite réserver l'équipement suivant :\n\nRéférence: {equipement.Reference}\nÉtat: {equipement.get_Etat_display()}\nDate d'Acquisition: {equipement.Date_Acquisition}\nMarque: {equipement.Marque}\nLaboratoire: {equipement.Laboratoire}\nVille de Laboratoire: {equipement.Laboratoire.Localisation}\n\nCordialement,\n{nom}"

            context = {
                'equipement': equipement,
                'form': form,
                'reservation_message': reservation_message,
            }
            message_reservation = MessageReservation.objects.create(
                nom=nom,  
                email=email,
                message=reservation_message,
                equipement=equipement,
            )

            return render(request, 'visiteur/equi.html', context=context)
    else:
        if request.user.is_authenticated:
            form = ContactForm(initial={
                'nom': request.user.get_full_name(),
                'email': request.user.email,
                'message': f"Bonjour,\n\nJe souhaite réserver l'équipement suivant :\n\nRéférence: {equipement.Reference}\nÉtat: {equipement.get_Etat_display()}\nDate d'Acquisition: {equipement.Date_Acquisition}\nMarque: {equipement.Marque}\nLaboratoire: {equipement.Laboratoire}\nVille de Laboratoire: {equipement.Laboratoire.Localisation}\n\nCordialement,\n{request.user.get_full_name()}",
            })
        else:
            form = ContactForm()

    context = {
        'equipement': equipement,  
        'form': form,  
    }

    return render(request, 'visiteur/contacter_labo.html', context)


def liste_messages_reservation(request):
    messages_reservation = MessageReservation.objects.all().order_by('-date_reservation')
    context = {
        'messages_reservation': messages_reservation,
    }
    return render(request, 'visiteur/liste_messages_reservation.html', context=context)
    
def envoyer_email_laboratoire(request, message_id):
    try:
        message = get_object_or_404(MessageReservation, id=message_id)
        laboratoire = message.equipement.Laboratoire
        sujet = "Demande de réservation d'équipement"
        contenu = message.message

        # Utilisez les paramètres d'e-mail configurés dans settings.py
        send_mail(sujet, contenu, settings.EMAIL_HOST_USER, [laboratoire.Email])

        return redirect('liste_messages_reservation')  # Redirige où vous voulez après l'envoi de l'e-mail
    except (SMTPException, gaierror) as e:
        # Gérer l'exception en fonction de vos besoins
        return HttpResponse("Une erreur s'est produite lors de l'envoi de l'e-mail.")
def supprimer_message_reservation(request):
    if request.method == 'POST':
        message_id = request.POST.get('message_id')
        message = get_object_or_404(MessageReservation, pk=message_id)
        message.delete()
        return redirect('liste_messages_reservation')
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})