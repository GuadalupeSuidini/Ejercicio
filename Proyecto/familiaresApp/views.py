from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from familiaresApp.models import Familia
# Create your views here.


def vistaPlantilla1 (requests):
    plantilla = loader.get_template('Plantilla1.html')
    documento = plantilla.render()
    return HttpResponse(documento)


def familiares(self,nombre,parentezco,edad,fechaNacimiento):
    familiares = Familia(nombre=nombre,parentezco=parentezco,edad=edad,fechaNacimiento=fechaNacimiento)
    familiares.save()
    return HttpResponse(f"se creo una neva persona: nombre: {familiares.nombre}, parentezco: {familiares.parentezco}")



