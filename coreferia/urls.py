from django.urls import path, include
from .views import home ,contacto, productos,ReportesVentas,reporteMenu, nuevo_producto, modificar_producto,eliminar_producto,venta_producto,compra,login, registrar_cl_externo, registro, registrar_productor, registrar_cl_interno,registrar_consultor
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),        
    path('registrar_cl_externo/', registrar_cl_externo.as_view(), name='registrar_cl_externo'),
    path('registro/', registro, name="registro"),
    path('registrar_productor/', registrar_productor.as_view(), name="registrar_productor"),
    path('registrar_cl_interno/', registrar_cl_interno.as_view(), name="registrar_cl_interno"),
    path('registrar_consultor/', registrar_consultor.as_view(), name="registrar_consultor"),
    path('productos/', productos, name="productos"),
    path('ReportesVentas/', ReportesVentas, name="ReportesVentas"),
    path('reporteMenu/', reporteMenu, name="reporteMenu"),
    path('nuevo_producto/', nuevo_producto, name="n_producto"),
    path('modificar_producto/<cod_prod>/', modificar_producto, name="m_producto"),
    path('eliminar_producto/<cod_prod>/', eliminar_producto, name="e_producto"),
    path('venta_producto/', venta_producto, name="v_producto"),
    path('compra/', compra, name="compra"),

    
]

