from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
from django.core.mail import send_mail
from django.conf import settings
from gestionPedidos.forms import formularioContacto
# Create your views here.

def buscar_producto(request):
    return render(request, "buscar_producto.html")

def buscar(request): #para ver si la informacion llega al servido 
    if request.GET['prd']:
        #mensaje="Articulo buscado: %r" %request.GET['prd']
        producto=request.GET['prd']
        if len(producto)<20:
            articulos=Articulos.objects.filter(nombre__icontains=producto)
            return render(request, "respuesta_producto.html",{"articulos": articulos, "query": producto})
        else:
            mensaje="lo escrito es demasiado largo"
    else:
        mensaje="no ingreso nada"
    return HttpResponse(mensaje)

#formulario de contacto
def contacto(request):
    if request.method=="POST":
        miformulario=formularioContacto(request.POST)
        #subject=request.POST["asunto"]
        #message=request.POST["mensaje"]+" "+ request.POST["email"]
        #email_from=settings.EMAIL_HOST_USER
        #recipient_list=["mily.mamani.1225@gmail.com"]
        #send_mail(subject,message,email_from,recipient_list)
        #return render(request,"gracias.html")
        if miformulario.is_valid():
            inform=miformulario.cleaned_data #toda la inf esta guardada
            send_mail(inform['asunto'],inform['mensaje'],inform.get('email',''),['mily.mamani.1225@gmail.com'],)# rescatamos los campos
            return render(request,"gracias.html")
    else:
        miformulario=formularioContacto()
    return render(request, "formulario_contacto.html",{"form": miformulario})#creamos un formulario
    #return render(request,"contacto.html")
