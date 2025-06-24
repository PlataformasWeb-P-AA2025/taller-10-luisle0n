from django.shortcuts import render, redirect
from .models import Parroquia, BarrioCiudadela
from .forms import ParroquiaForm, BarrioCiudadelaForm
 #Vista inicial que muestra las parroquias y barrios, y permite crear nuevos
def vista_inicial(request):
    # Obtener todas las parroquias y barrios de la base de datos
    parroquias = Parroquia.objects.all()
    barrios = BarrioCiudadela.objects.all()

    # Manejar la creación de nuevos objetos de parroquias o barrios a través de los formularios
    if request.method == 'POST':
        # Si el formulario de crear parroquia es enviado
        if 'crear_parroquia' in request.POST:
            form_parroquia = ParroquiaForm(request.POST)
            if form_parroquia.is_valid():  # Validar el formulario
                form_parroquia.save()  # Guardar la nueva parroquia
                return redirect('vista_inicial')  # Redirigir a la misma página para ver los cambios
        # Si el formulario de crear barrio es enviado
        elif 'crear_barrio' in request.POST:
            form_barrio = BarrioCiudadelaForm(request.POST)
            if form_barrio.is_valid():  # Validar el formulario
                form_barrio.save()  # Guardar el nuevo barrio
                return redirect('vista_inicial')  # Redirigir a la misma página para ver los cambios
    else:
        form_parroquia = ParroquiaForm()  # Formulario vacío para crear una parroquia
        form_barrio = BarrioCiudadelaForm()  # Formulario vacío para crear un barrio

    # Pasar los datos a la plantilla para mostrar las parroquias, barrios y formularios
    return render(request, 'vista_inicial.html', {
        'parroquias': parroquias,
        'barrios': barrios,
        'form_parroquia': form_parroquia,
        'form_barrio': form_barrio,
    })

# Vista que lista todas las parroquias y sus barrios
def lista_parroquias_y_barrios(request):
    parroquias = Parroquia.objects.all()
    
    # Obtener los barrios asociados a cada parroquia
    for parroquia in parroquias:
        parroquia.barrios = BarrioCiudadela.objects.filter(parroquia=parroquia)
    
    # Pasar la lista de parroquias y barrios a la plantilla
    return render(request, 'listarBP.html', {'parroquias': parroquias})

# Vista que lista todos los barrios
def lista_barrios(request):
    barrios = BarrioCiudadela.objects.all()  # Obtener todos los barrios
    return render(request, 'lista_barrios.html', {'barrios': barrios})  # Pasar la lista de barrios a la plantilla

# Vista para crear una nueva parroquia
def crear_parroquia(request):
    if request.method == 'POST':
        form = ParroquiaForm(request.POST)  # Crear el formulario con los datos POST
        if form.is_valid():  # Si el formulario es válido
            form.save()  # Guardar la nueva parroquia
            return redirect('lista_parroquias')  # Redirigir a la página de listar parroquias
    else:
        form = ParroquiaForm()  # Si no es POST, mostrar un formulario vacío
    
    # Pasar el formulario a la plantilla
    return render(request, 'formulario_parroquia.html', {'form': form})

# Vista para crear un nuevo barrio
def crear_barrio(request):
    if request.method == 'POST':
        form = BarrioCiudadelaForm(request.POST)  # Crear el formulario con los datos POST
        if form.is_valid():  # Si el formulario es válido
            form.save()  # Guardar el nuevo barrio
            return redirect('lista_barrios')  # Redirigir a la página de listar barrios
    else:
        form = BarrioCiudadelaForm()  # Si no es POST, mostrar un formulario vacío
    
    # Pasar el formulario a la plantilla
    return render(request, 'formulario_barrio.html', {'form': form})