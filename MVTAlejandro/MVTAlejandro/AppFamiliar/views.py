from django.template import Template, Context
from django.shortcuts import render
from django.http import HttpResponse
from AppFamiliar.models import Familiar
from datetime import datetime

# Create your views here.

def familiares(self):

    familiares = Familiar(nombre="Daniel", apellido="Arrighi", dni=874984, fecha="20/04/2022")
    familiares.save()
    texto=f"<br>Familiar Padre agregado: {familiares.nombre} {familiares.apellido} {familiares.dni}</br>\n"
    familiares = Familiar(nombre="Myriam", apellido="Arrighi", dni=1640785)
    familiares.save()
    texto+=f"<br>Familiar Madre agregado: {familiares.nombre} {familiares.apellido} {familiares.dni}</br>\n"
    familiares = Familiar(nombre="Santina", apellido="Molinari", dni=842182)
    familiares.save()
    texto+=f"<br>Familiar Abuelo agregado: {familiares.nombre} {familiares.apellido} {familiares.dni}</br>\n"

    html=open("E:/MVTAlejandro/MVTAlejandro/MVTAlejandro/templates/Template.html")

    plantilla=Template(html.read())

    html.close()

    micontexto=Context(familiares)

    texto+=plantilla.render(micontexto)
    return HttpResponse(texto)

    