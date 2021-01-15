from django.contrib import admin
from django.urls import path
from proyectowebApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name="Home"),
    path('servicios/',views.servicios,name="Servicios"),
    path('tienda/',views.tienda,name="Tienda"),
    path('block/',views.block,name="Block"),
    path('contacto/',views.contacto,name="Contacto"),
]