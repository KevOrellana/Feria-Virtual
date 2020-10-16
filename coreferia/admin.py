from django.contrib import admin
from .models import Administrador,Orden,DetalleOrden,Bodega,ClExterno,ClInterno,Consultor,ContratoP,ContratoT,DetalleFactura,Factura,OfertaT,Pedido,Perfil,Productor,RegistroPago,Reporte,Subasta,Transportista,AuthUser,Producto

# Register your models here.


admin.site.register(Administrador)
admin.site.register(AuthUser)
admin.site.register(Bodega)
admin.site.register(ClExterno)
admin.site.register(ClInterno)
admin.site.register(Consultor)
admin.site.register(ContratoP)
admin.site.register(ContratoT)
admin.site.register(DetalleFactura)
admin.site.register(Factura)
admin.site.register(OfertaT)
admin.site.register(Pedido)
admin.site.register(Perfil)
admin.site.register(Producto)
admin.site.register(Productor)
admin.site.register(RegistroPago)
admin.site.register(Reporte)
admin.site.register(Subasta)
admin.site.register(Transportista)
admin.site.register(Orden)
admin.site.register(DetalleOrden)


