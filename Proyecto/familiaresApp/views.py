from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
# Create your views here.


def vistaPlantilla1 (requests):
    plantilla = loader.get_template('Plantilla1.html')
    documento = plantilla.render()
    return HttpResponse(documento)

