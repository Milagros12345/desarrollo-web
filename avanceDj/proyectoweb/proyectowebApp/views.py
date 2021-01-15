from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request,"proyectowebApp/home.html")

def servicios(request):
    return render(request,"proyectowebApp/servicios.html")
def tienda(request):
   return render(request,"proyectowebApp/tienda.html")
def block(request):
    return render(request,"proyectowebApp/block.html")

def contacto(request):
    return render(request,"proyectowebApp/contacto.html")