from django.forms import ModelForm  # Importa el formulario basado en modelos de Django
from .models import Parroquia, BarrioCiudadela  # Importa los modelos Parroquia y BarrioCiudadela

# Formulario para crear o editar una Parroquia
class ParroquiaForm(ModelForm):
    # Clase Meta para indicar el modelo y los campos del formulario
    class Meta:
        model = Parroquia  # Define que este formulario corresponde al modelo Parroquia
        fields = ['nombre', 'ubicacion', 'tipo']  # Especifica los campos que se incluirán en el formulario

# Formulario para crear o editar un BarrioCiudadela
class BarrioCiudadelaForm(ModelForm):
    # Clase Meta para indicar el modelo y los campos del formulario
    class Meta:
        model = BarrioCiudadela  # Define que este formulario corresponde al modelo BarrioCiudadela
        fields = ['nombre', 'numero_viviendas', 'numero_parques', 'numero_edificios_residenciales', 'parroquia']  # Especifica los campos que se incluirán en el formulario
