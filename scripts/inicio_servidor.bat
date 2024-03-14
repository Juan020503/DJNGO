rem Activa el entorno virtual
call entorno_de_pruebas_django\Scripts\activate

rem Cambia al directorio del proyecto
cd proyecto_django_pruebas

rem Ejecuta el servidor Django
start /B python manage.py runserver

rem Vuelve a la carpeta principal
cd ..