from django.http import HttpResponse
from django.template import Template, Context, loader


def saludo(request):
    return HttpResponse("Holis")


def saludo2(request):
    return HttpResponse("<h1>Tienda</h1>")


def saludo3(self):
    nombre = "Felipe"
    apellido = "cerquin"
    diccionario = {
        "nombre": nombre,
        "apellido": apellido
    }
    plantilla = loader.get_template("template1.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)
