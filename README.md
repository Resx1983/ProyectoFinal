# Reseña sobre Rimworld
## Descripción del proyecto
Este es un proyecto realizado como proyecto final para mi clase de Lógica de Programación I ([Docente: Daniel Felipe Agudelo Molina](https://github.com/DanielDev87)). En él podemos encontrar una página 
hablando sobre Rimworld, su comunidad y su contenido. La finalidad de este proyecto es utilizar cierta lógica de programación aprendida junto con

## Instalación
Para instalar este proyecto, deberás seguir los siguientes pasos:
1. Descargar el archivo de este repositorio
2. Descomprimir el archivo Zip

## Tecnologías utilizadas

* [HTML](https://developer.mozilla.org/es/docs/Web/HTML)
* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/2.1.x/)
* [Boostrap](https://getbootstrap.com/)
* [Jinja2](https://palletsprojects.com/p/jinja/)

## Contribuciones 
Si quisieras contribuir con este proyecto o agregarle nuevas vistas con contenido, deberás tener en cuenta los bloques jinja:

{% extends "base.html" %}

{% block title %} "Título de la nueva vista" {% endblock %}

{% block content%}
 
{% endblock %}

Agrega nuevos archivos HTML con esta estructura dentro de la carpeta "templates", luego, dentro de app.py, crear una función para la nueva vista.

