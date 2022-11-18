from django.shortcuts import render
from app_colegio.models import alumnos

def inicio(request):
    return render (request, 'index.html')

def registrar(request):

    if request.method == 'POST':

        rut = request.POST['txtRut']
        nom = request.POST['txtNom']
        ape = request.POST['txtApe']
        sex = request.POST['opSex']
        cur = request.POST['cboCurso']
        eda = request.POST['txteda']
        ciu = request.POST['cboCiu']
        com = request.POST['txtComu']

        comprobarRut = alumnos.objects.filter(rut=rut)

        if comprobarRut:
            datos = { 'r2' : 'El rut ('+rut+') ya se encuentra registrado!!!' }
            return render(request, 'form_registrar.html', datos)
        else:
            alum = alumnos(rut=rut, nombre=nom, apellidos=ape, sexo=sex, curso=cur, edad=eda, ciudad=ciu, comuna=com)
            alum.save()
            datos = { 'r' : 'El alumno se registró correctamente!!!' }
            return render(request, 'form_registrar.html', datos)
    return render(request, 'form_registrar.html')

def listado(request):
    return render(request, 'listado.html')