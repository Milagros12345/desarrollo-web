from django.contrib import admin
from gestionPedidos.models import clientes, Articulos, pedidos

# Register your models here.
class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre","direccion","telefono")
    search_fields=("nombre","telefono")
class ArticulosAdmin(admin.ModelAdmin):
    list_filter=("seccion",)

class PedidosAdmin(admin.ModelAdmin):
    list_display=("numero","fecha")
    list_filter=("fecha",)# le agregamos , xq es una tupla
    date_hierarchy="fecha"
admin.site.register(clientes, ClientesAdmin)#para que sea disponible la tabla clientes 
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(pedidos, PedidosAdmin)
