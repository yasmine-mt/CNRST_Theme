
from django.urls import path
from . import views
urlpatterns = [
    path('',views.accueil_visiteur , name='accueil_visiteur'),
    path('search/', views.search_equipments2, name='search_equipments2'), 
    path('contact_laboratoire/<int:laboratoire_id>/', views.contact_laboratoire, name='contact_laboratoire'),
]
