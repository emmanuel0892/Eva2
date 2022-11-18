from django.shortcuts import render

def inicio(request):
    return render (request, 'index.html')

def registrar(request):
    return render(request, 'form_registrar.html')

def listado(request):
    return render(request, 'listado.html')