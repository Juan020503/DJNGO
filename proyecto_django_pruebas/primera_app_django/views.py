from django.shortcuts import render
from . forms import UsuarioForm

def pagina1(request):
    return render(request,"pagina1.html")

def pagina2(request):
    return render(request,"pagina2.html")

from django.shortcuts import render
from . forms import UsuarioForm

def formulario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            # hacer algo después de guardar los datos del usuario
    else:
        form = UsuarioForm()
    return render(request, 'formulario.html', {'form': form})

from django.shortcuts import render
from .models import Tienda, Producto

def tiendas(request):
    tiendas = Tienda.objects.all()
    return render(request, 'tiendas.html', {'tiendas': tiendas})

def productos(request, tienda_id):
    tienda = Tienda.objects.get(id=tienda_id)
    productos = Producto.objects.filter(tienda=tienda)
    return render(request, 'productos.html', {'tienda': tienda, 'productos': productos})

from django.shortcuts import render
from .models import MensajeContacto

def ver_mensajes_contacto(request):
    mensajes = MensajeContacto.objects.all()
    return render(request, 'app_contacto/ver_mensajes_contacto.html', {'mensajes': mensajes})

