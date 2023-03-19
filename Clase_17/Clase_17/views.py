from django.http import HttpResponse
from datetime import datetime as dt
from django.template import Template, Context, loader

def saludo (request):   
    return HttpResponse("Hola comisión")

def segunda_vista(request):
    return HttpResponse("<br><br><br>Esta es la segunda vista")

def dia(request):
    hoy = dt.now()
    return HttpResponse(f"El día y hora de hoy es:<br>{hoy}")

def mostrar_nombre(request,nombre):
    texto = "Tu nombre es:"
    return HttpResponse(f"{texto} {nombre}")

def probando_template(request):

    notas = [10, 9, 8, 4]
    mis_datos = {"nombre":"Esteban", "apellido":"Acevedo", "notas": notas}

#    mihtml = open("./plantillas/template1.html")
#    plantilla = Template(mihtml.read())
#    mihtml.close()

    plantilla = loader.get_template("template1.html")
    
#    mi_contexto = Context(mis_datos)
    
#    documento = plantilla.render(mi_contexto)

    documento = plantilla.render(mis_datos)
    return HttpResponse(documento)