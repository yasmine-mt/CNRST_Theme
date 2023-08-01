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
pip install django-filter , pip install Django ,pip install Django-auditlog,  pip install mysqlclient

# Urls :
  # Accés a l'interface Admin de Django
    http://127.0.0.1:8000/admin 
    On peut gérer tous les comptes de la BD avec les autres tables 


