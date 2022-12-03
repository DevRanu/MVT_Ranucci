from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from AppFamily.models import *
import datetime

# Create your views here.

def inicio(request):
    archivo=open(r'C:\Users\Nahue\Documents\Coding\Envs\MVT_Ranucci\AppFamily\templates\inicio.html')
    template=Template(archivo.read())
    archivo.close()
    contexto=Context()
    documento=template.render(contexto)
    return HttpResponse(documento)

def hermanotmplt(request):
    herman= Hermano(nombre="Bruce Wayne", edad=40, nacido=datetime.date(1982,5,8))
    herman.save()
    diccio={"nombre":herman.nombre, "edad":herman.edad, "nacimiento":herman.nacido}
    archivo=open(r'C:\Users\Nahue\Documents\Coding\Envs\MVT_Ranucci\AppFamily\templates\hermano.html')
    template=Template(archivo.read())
    archivo.close()
    contexto=Context(diccio)
    documento=template.render(contexto)
    return HttpResponse(documento)

def primitmplt(request):
    primi= Primo(nombre="Tony Stark", edad=38, nacido=datetime.date(1984,11,16))
    primi.save()
    diccio={"nombre":primi.nombre, "edad":primi.edad, "nacimiento":primi.nacido}

    archivo=open(r'C:\Users\Nahue\Documents\Coding\Envs\MVT_Ranucci\AppFamily\templates\primo.html')
    template=Template(archivo.read())
    archivo.close()
    contexto=Context(diccio)
    documento=template.render(contexto)
    return HttpResponse(documento)

def sobritmplt(request):
    sobrin= Sobrino(nombre="Peter Parker", edad=19, nacido=datetime.date(2003,7,11))
    sobrin.save()
    diccio={"nombre":sobrin.nombre, "edad":sobrin.edad, "nacimiento":sobrin.nacido}

    archivo=open(r'C:\Users\Nahue\Documents\Coding\Envs\MVT_Ranucci\AppFamily\templates\sobrino.html')
    template=Template(archivo.read())
    archivo.close()
    contexto=Context(diccio)
    documento=template.render(contexto)
    return HttpResponse(documento)