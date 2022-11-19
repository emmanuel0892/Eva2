from django.shortcuts import render, redirect
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

    alum = alumnos.objects.all().values()
    datos = {
        'alum':alum
    }

    return render(request, 'listado.html',datos)

def eliminar(request, id):
    try:
        alumn = alumnos.objects.get(id=id)
        alumn.delete()

        alum = alumnos.objects.all().values()
        datos = {
            'alum':alum,
            'r':'Alumno Eliminado Correctamente!!!',
        }

        return render(request, 'listado.html', datos)
    except:
        pass

#Vista Actualizar
def actualizar(request, id):
    try:
        alumn = alumnos.objects.get(id=id)
        datos = {
            'alumn':alumn,
        }
        return render(request, 'form_actualizar.html', datos)

    except:
        alum = alumnos.objects.all().values()
        datos = {
            'alum':alum
        }
    return render(request, 'listado.html',datos)


#guardar datos actualizados
def modificar(request, id):
    
    try:
        nom = request.POST['txtNom']
        ape = request.POST['txtApe']
        sex = request.POST['opSex']
        cur = request.POST['cboCurso']
        eda = request.POST['txteda']
        ciu = request.POST['cboCiu']
        com = request.POST['txtComu']

        alumn = alumnos.objects.get(id=id)
        alumn.nombre = nom
        alumn.apellidos = ape
        alumn.sexo = sex
        alumn.curso = cur
        alumn.edad = eda
        alumn.ciudad = ciu
        alumn.comuna = com
        alumn.save()

        alum = alumnos.objects.all().values()
        datos = {
            'alum':alum,
            'r':'Datos actualizados correctamente!!!',
        }

        return render(request, 'listado.html',datos)
    except:
        alum = alumnos.objects.all().values()
        datos = {
            'alum':alum,
            'r2':'Datos actualizados correctamente!!!',
        }
        return render(request, 'listado.html',datos)
