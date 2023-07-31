
from django.urls import path
from . import views
urlpatterns = [
    path('accueil_visiteur/',views.accueil_visiteur , name='accueil_visiteur'),
]
