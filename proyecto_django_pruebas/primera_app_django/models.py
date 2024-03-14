from django.db import models

class Usuario(models.Model):
  
    nombre_usuario = models.CharField(max_length=30, unique=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

   
    edad = models.PositiveIntegerField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    altura = models.FloatField()

    fecha_nacimiento = models.DateField()
    ultimo_login = models.DateTimeField(auto_now=True)

 
    esta_activa = models.BooleanField(default=True)
    es_personal = models.BooleanField(default=False)


    OPCIONES_ROL = [
        ('usuario', 'Usuario normal'),
        ('admin', 'Administrador'),
    ]
    roles = models.CharField(max_length=7, choices=OPCIONES_ROL, default='usuario')

from django.db import models

class Tienda(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre

from django.db import models

class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=255)
    correo = models.EmailField()
    mensaje = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre