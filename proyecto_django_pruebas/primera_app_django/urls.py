from django.urls import path
from . import views

urlpatterns =[
    path('', views.tiendas, name='tiendas'),
    path('formulario/', views.formulario, name = 'formulario'),
    path('pagina1/', views.pagina1, name = 'pagina1'),
    path('pagina2/', views.pagina2, name = 'pagina2'),
    path('tiendas/<int:tienda_id>/productos/', views.productos, name='productos'),
]
