from django.shortcuts import render
from .models import Alumnos, Comentario, ComentarioContacto, Archivos
from .forms import AlumnosForm, ComentarioContactoForm, FormArchivos
from django.shortcuts import get_object_or_404
import datetime
from django.contrib import messages


def registroAlumnos(request):
    alumno = Alumnos.objects.all()
    return render(request, 'registros/registroAlumnos.html', {'alumno': alumno})

def registrarAlumno(request):
    if request.method == 'POST':
        form = AlumnosForm(request.POST)
        if form.is_valid():
            form.save()
            alumnos = Alumnos.objects.all()
            return render(request, 'registros/principal.html', {'alumnos': alumnos})
        form = AlumnosForm()
        # Si algo sale mal se reenvia al formulario los datos ingresados
        return render(request, 'registros/registroAlumnos.html', {'form': form})

# Eliminar Alumno
def eliminarAlumno(request, id, confirmacion2 = 'registros/confirmarEliminacionAlumno.html'):
    alumno = get_object_or_404(Alumnos, id=id)
    if request.method == 'POST':
        alumno.delete()
        alumnos = Alumnos.objects.all()
        return render(request, 'registros/principal.html', {'alumnos': alumnos})
    return render(request, confirmacion2, {'object': alumno})

def consultarAlumno(request, id):
    alumno = Alumnos.objects.get(id=id)
    return render(request, 'registros/formEditarAlumno.html', {'alumno': alumno})


# Eliminar//

# Editar
def editarAlumno(request, id):
    alumno = get_object_or_404(Alumnos, id=id)
    form = AlumnosForm(request.POST, instance=alumno)
    
    if form.is_valid():
            form.save()
            alumnos = Alumnos.objects.all()
            return render(request, 'registros/principal.html', {'alumnos': alumnos})
    return render(request, 'registros/formEditarAlumno.html', {'alumno':alumno})

def registros(request):
    alumnos=Alumnos.objects.all()
    return render(request, 'registros/principal.html', {'alumnos':alumnos})


def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save()
            comentarios = ComentarioContacto.objects.all()
            return render(request, 'registros/comentarios.html', {'comentarios': comentarios})
        form = ComentarioContactoForm()
        # Si algo sale mal se reenvia al formulario los datos ingresados
        return render(request, 'registros/contacto.html', {'form': form})
    
    # Eliminar Comentario
def eliminarComentarioContacto(request, id, 
    confirmacion = 'registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method == 'POST':
        comentario.delete()
        comentarios = ComentarioContacto.objects.all()
        return render(request, 'registros/comentarios.html', {'comentarios': comentarios})
    return render(request, confirmacion, {'object': comentario})

def consultarComentario(request, id):
    comentario = ComentarioContacto.objects.get(id=id)
    return render(request, 'registros/formEditarComentario.html', {'comentario': comentario})
# Eliminar//

# Editar
def editarComentario(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoForm(request.POST, instance=comentario)
    
    if form.is_valid():
        form.save()
        comentarios = ComentarioContacto.objects.all()
        return render(request, 'registros/comentarios.html', {'comentarios': comentarios})
    return render(request, 'registros/formEditarComentario.html', {'comentario':comentario })


# /Editar


def contacto(request):
    return render(request, "registros/contacto.html")


def coment(request):
    comentarios = ComentarioContacto.objects.all()
    return render(request, 'registros/comentarios.html', {'comentarios': comentarios})

def consultar1(request):
    #con una sola condición
    alumnos=Alumnos.objects.filter(carrera="TI")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar2(request):
    #
    alumnos=Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar3(request):
    alumnos=Alumnos.objects.all().only( "nombre", "carrera", "turno", "imagen")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar4(request):
    alumnos=Alumnos.objects.filter(turno__contains="Vesp")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar5(request):
    alumnos=Alumnos.objects.filter(nombre__in=["Juan", "Ana"])
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar6(request):
    fechaInicio = datetime.date(2022, 7, 1)
    fechaFin = datetime.date(2022, 7, 14)
    alumnos=Alumnos.objects.filter(created__range=(fechaInicio, fechaFin))
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar7(request):
    alumnos=Alumnos.objects.filter(comentario__coment__contains="No me sirve aiiuda!!!!!")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            archivo = request.FILES['archivo']
            insert = Archivos(titulo=titulo, descripcion=descripcion, archivo=archivo)
            insert.save()
            return render(request,"registros/archivos.html")
        else:
            messages.error(request,"Error al procesar el formulario")
    else:
        return render(request,"registros/archivos.html",{'archivo':Archivos})

def consultasSQL(request):
    alumnos=Alumnos.objects.raw('Select id, matricula, nombre, carrera, turno, imagen FROM registros_alumnos WHERE carrera="TI" ORDER BY turno DESC')
    return render(request,"registros/consultas.html", {'alumnos':alumnos})

def seguridad(request, nombre=None):
    nombre=request.GET.get('nombre')
    return render(request, 'registros/seguridad.html',
    {'nombre':nombre})