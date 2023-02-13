from django.shortcuts import render
from AppCoders.models import Curso
from django.http import HttpResponse

def curso(self):

    curso= Curso(nombre="desarollo web",camada="19881")
    curso.save()
    documentoDeTexto=f"---> cursos {curso.nombre}    camada: {curso.camada}"

    return HttpResponse(documentoDeTexto)