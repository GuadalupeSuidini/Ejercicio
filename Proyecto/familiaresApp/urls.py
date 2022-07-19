


from django.urls import path
from familiaresApp.views import listaFamiliares, familiares

urlpatterns = [
    path('cargaDePersonas/<nombre>/<parentezco>/<edad>/<fechaNacimiento>', familiares),
    path('lista/',listaFamiliares)
]
