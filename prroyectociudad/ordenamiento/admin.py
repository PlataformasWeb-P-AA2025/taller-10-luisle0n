from django.contrib import admin

# Importar las clases del modelo
from .models import Parroquia, BarrioCiudadela

# Clase admin para el modelo Parroquia
class ParroquiaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'tipo')
    search_fields = ('nombre',)
    list_filter = ('ubicacion', 'tipo')

# Registrar el modelo Parroquia con su clase admin
admin.site.register(Parroquia, ParroquiaAdmin)


# Clase admin para el modelo BarrioCiudadela
class BarrioCiudadelaAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en el listado
    list_display = (
        'nombre', 'numero_viviendas', 'numero_parques',
        'numero_edificios_residenciales', 'parroquia'
    )
    search_fields = ('nombre',)
    list_filter = ('numero_parques', 'parroquia')
    raw_id_fields = ('parroquia',)

# Registrar el modelo BarrioCiudadela con su clase admin
admin.site.register(BarrioCiudadela, BarrioCiudadelaAdmin)
