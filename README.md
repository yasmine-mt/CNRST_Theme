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
    On peut gérer tous les comptes de la BD avec les autres tables {ajouter des nouveaux utilisateurs ...}
    Apres l'accés, on doit impérativement ajouter nos utilisateurs dans la partie User profiles et choisir leur role selon notre besoin. 

 
# Autre info
  On peut accéder à l'interface admin personnalisée depuis le bouton superviseur 

  pour modifier l'email qui envoie le lien de verification , on doit modifier dans le fichier settings.py du projet pour remplacer EMAIL_HOST_USER  par le nouveau email et changer EMAIL_HOST_PASSWORD .



