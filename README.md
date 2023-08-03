# Installation
Après avoir clôné le repo :

    # Requirements
    python 3.6
    pip3
    virtualenv
    # Recommandé : créez un environnement virtuel
    $ virtualenv venv
    $ venv\Scripts\activate
    
    # Initialisez la DB
    $ python manage.py makemigrations
    $ python manage.py migrate
    
    # Lancez le serveur de dev
    $ python manage.py runserver

Le site sera accessible à l'adresse http://localhost:8000/.
# Technologies utilisées:
Python
Django
Bootstrap
JavaScript
HTML
CSS
# Database
MySQL
# Modules Python supplémentaires requis (Installation depuis la ligne de commande ) :
  # pip install  
    Django 
    Django-auditlog
    Django-filter
    mysqlclient

# Urls :

  # Accés a l'interface Admin de Django
    http://127.0.0.1:8000/admin 
    On peut gérer tous les comptes de la BD avec les autres tables 
    **Nom d’utilisateur & Mot de passe : admin**

  # Accés a l'interface Visiteur de Django
    Nom d’utilisateur : visiteur
    Mot de passe : gestion2023

# Autre info
  On peut accéder à l'interface admin personnalisée depuis le bouton superviseur 
   



