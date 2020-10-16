from django.shortcuts import render, redirect
from .models import Producto,Productor,Orden,ClExterno,ClInterno
from django.db import connection
import cx_Oracle
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from .forms import  CustomUserForm, ClExternoForm, ProductorForm, ClInternoForm,ConsultorForm
import base64
# Create your views here.

def home(request):
    
        return render(request, 'coreferia/homeProductor.html')
        
def contacto(request):
    return render(request, 'coreferia/contacto.html')

def registro(request):
    
    return render(request, 'registration/registro.html')
    
def login(request):
    
    return render(request, 'coreferia/login.html')

def logout(request):

    return redirect(to='home')

@login_required
def productos(request):
        
    
    productos = Producto.objects.all()
    data = {
        'productos':productos
    }
    
    return render(request, 'coreferia/productos.html', data)

@login_required
def reporteMenu(request):

    return render(request, 'coreferia/reporteMenu.html')
@login_required
def ReportesVentas(request):
    
    print(listado_reporte_orden())# para verificar que carguen los archivos
    data = {
        'orden':listado_reporte_orden()        
    }

    
    return render(request, 'coreferia/ReportesVentas.html', data)

def listado_reporte_orden():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("sp_listar_orden",[out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    
    return lista


@login_required
def nuevo_producto(request):
    
    data = {
        'form':ProductoForm()
    }
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            print(form.errors)
            return render(request, 'coreferia/nuevo_producto.html', data)
        else:
            return render(request, 'coreferia/nuevo_producto.html', data)

    return render(request, 'coreferia/nuevo_producto.html', data)


@login_required
def listado_producto():
    django_cursor = connection.cursor()
    cursor= django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    

    cursor.callproc("sp_listar_producto",[out_cur])

    lista = []
    for fila in out_cur:
        data ={
            'data':fila,
            'foto_prod':str(base64.b64encode(fila[4].read()), 'utf-8')
        }    
        
        lista.append(data)
    return lista    



@login_required
def modificar_producto(request, cod_prod):
    producto = Producto.objects.get(cod_prod=cod_prod)
    data = {
        'form': ProductoForm(instance=producto)
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Actualizado Correctamente"
            data['form'] = formulario 
    return render(request, 'coreferia/modificar_producto.html', data)

def eliminar_producto(request, cod_prod):
    producto = Producto.objects.get(cod_prod=cod_prod)
    producto.delete()
    
    return redirect(to="productos")
@login_required
def venta_producto(request):
    data = {
        'producto1':listado_venta1,
        'producto2':listado_venta2,
        'producto3':listado_venta3,
        'producto4':listado_venta4,
        'producto5':listado_venta5,
        'producto6':listado_venta6
    }
    return render(request, 'coreferia/venta_producto.html',data)

def compra(request):
    
    return render(request, 'coreferia/compra.html')



def listado_venta1():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_VENTA1", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    
    return lista
def listado_venta2():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_VENTA2", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    
    return lista
def listado_venta3():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_VENTA3", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    
    return lista
def listado_venta4():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_VENTA4", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    
    return lista
def listado_venta5():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_VENTA5", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    
    return lista
def listado_venta6():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_VENTA6", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    
    return lista




class registrar_productor(CreateView):

    template_name = 'registration/registrar_productor.html'

    form_class = ProductorForm
    second_form_class = CustomUserForm

    def get_context_data(self, **kwargs):
        contex = super(registrar_productor, self).get_context_data(**kwargs)
        if 'form' not in contex:
            contex['form'] = self.form_class(self.request.GET)
        if 'form2' not in contex:
            contex['form2'] = self.second_form_class(self.request.GET)
        return contex

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        
        
        #    print(form.errors) para probar los errores 
        print(form2.errors)
        #    print(form.is_valid()) para verificar si esta ingresando datos
        if form.is_valid() and form2.is_valid():
            print(form2)
            solicitud = form.save(commit=False)
            solicitud.persona = form2.save()
            solicitud.save()
            return redirect(to='home')
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))
        
class registrar_cl_interno(CreateView):

    template_name = 'registration/registrar_cl_interno.html'

    form_class = ClInternoForm
    second_form_class = CustomUserForm

    def get_context_data(self, **kwargs):
        contex = super(registrar_cl_interno, self).get_context_data(**kwargs)
        if 'form' not in contex:
            contex['form'] = self.form_class(self.request.GET)
        if 'form2' not in contex:
            contex['form2'] = self.second_form_class(self.request.GET)
        return contex

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            solicitud = form.save(commit=False)
            solicitud.persona = form2.save()
            solicitud.save()
            return redirect(to='home')
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))

class registrar_cl_externo(CreateView):
  #  data = {    
  #      'form':CustomUserForm()
  #  }
    template_name = 'registration/registrar_cl_externo.html'

    form_class = ClExternoForm
    second_form_class = CustomUserForm

    def get_context_data(self, **kwargs):
        contex = super(registrar_cl_externo, self).get_context_data(**kwargs)
        if 'form' not in contex:
            contex['form'] = self.form_class(self.request.GET)
        if 'form2' not in contex:
            contex['form2'] = self.second_form_class(self.request.GET)
        return contex

    def post(self, request, *args, **kwargs):
        self.object = self.get_object        
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            solicitud = form.save(commit=False)
            solicitud.persona = form2.save()
            solicitud.save()
            return redirect(to='home')
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))
 
 
 #registro del consultor
 #      
class registrar_consultor(CreateView):

    template_name = 'registration/registrar_consultor.html'

    form_class = ConsultorForm
    second_form_class = CustomUserForm

    def get_context_data(self, **kwargs):
        contex = super(registrar_consultor, self).get_context_data(**kwargs)
        if 'form' not in contex:
            contex['form'] = self.form_class(self.request.GET)
        if 'form2' not in contex:
            contex['form2'] = self.second_form_class(self.request.GET)
        return contex

    def post(self, request, *args, **kwargs):

        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            solicitud = form.save(commit=False)
            solicitud.persona = form2.save()
            solicitud.save()
            
            request.user.groups.name == "consultor"
            request.user.save()            
            return redirect(to='home')
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))
