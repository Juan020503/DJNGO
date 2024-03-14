from django.urls import path
from . import views

urlpatterns =[
    path('', views.tiendas, name='tiendas'),
    path('formulario/', views.formulario, name = 'formulario'),
    path('pagina1/', views.pagina1, name = 'pagina1'),
    path('contacto/', views.pagina2, name = 'contacto'),
    path('tiendas/<int:tienda_id>/productos/', views.productos, name='productos'),
    path('pagina2/', views.ver_mensajes_contacto, name='ver_mensajes_contacto'),
]


