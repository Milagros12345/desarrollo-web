from django.http import HttpResponse
import datetime
from django.template import Context, Template, loader
from django.shortcuts import render
class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

def saludo(request):
    per=Persona("ruth milagros","mamani apucusi")
    fecha=datetime.datetime.now()
    temasCurso=["plantilla","modelos","formularios","vista","despliegue"]
    #doc_externo=open("E:/avanceDj/proyecto01/proyecto01/plantilla/plantilla1.html")
    #plt=Template(doc_externo.read())
    #doc_externo.close()
    #doc_externo= loader.get_template("plantilla1.html")
    #ctx=Context({"nombre_p":per.nombre,"apellido_p":per.apellido,"fecha":fecha,"tema":temasCurso})# la clave y la variable que contiene ing
    #documento=doc_externo.render({"nombre_p":per.nombre,"apellido_p":per.apellido,"fecha":fecha,"tema":temasCurso})
   
    return render(request,"plantilla1.html",{"nombre_p":per.nombre,"apellido_p":per.apellido,"fecha":fecha,"tema":temasCurso})
def cursoC(request):
    fecha=datetime.datetime.now()
    return render(request,"hijo1.html",{"fecha": fecha})
def curso2(request):
    fecha2=datetime.datetime.now()
    return render(request,"hijo2.html",{"fecha": fecha2})
def despedida(request):
    return HttpResponse("chau amiga")
