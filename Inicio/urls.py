from django.urls import path
from Inicio import views

urlpatterns = [
    path('', views.inicio),
    path('bandas', views.bandas, name="Bandas"),
    path('discos', views.discos, name="Discos"),
    path('musicos', views.musicos, name="Musicos"),
    path('busqueda/', views.buscar, name="Buscar"),
]
