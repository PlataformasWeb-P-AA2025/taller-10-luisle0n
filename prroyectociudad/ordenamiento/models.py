from django.db import models  # Importa las clases necesarias para definir modelos en Django

# Modelo que representa una Parroquia
class Parroquia(models.Model):
    # Nombre de la parroquia (campo de texto con un límite de 30 caracteres)
    nombre = models.CharField(max_length=30)
    # Ubicación de la parroquia, puede ser algo como "norte", "sur", etc. (campo de texto de 10 caracteres)
    ubicacion = models.CharField(max_length=10)  
    # Tipo de parroquia, como "urbana" o "rural" (campo de texto de 10 caracteres)
    tipo = models.CharField(max_length=10)  

    # Método para representar el objeto Parroquia como una cadena de texto
    # Este método se utiliza cuando se llama a `str(parroquia)`
    def __str__(self):
        # Devuelve una representación concatenada de nombre, ubicación y tipo de la parroquia
        return "%s %s %s" % (self.nombre, self.ubicacion, self.tipo)


# Modelo que representa un Barrio o Ciudadela
class BarrioCiudadela(models.Model):
    # Nombre del barrio o ciudadela (campo de texto con un límite de 30 caracteres)
    nombre = models.CharField(max_length=30)
    # Número de viviendas en el barrio (campo numérico entero)
    numero_viviendas = models.IntegerField()
    # Número de parques en el barrio (campo numérico entero)
    numero_parques = models.IntegerField()
    # Número de edificios residenciales en el barrio (campo numérico entero)
    numero_edificios_residenciales = models.IntegerField()
    # Relación con la parroquia, un barrio está asociado a una parroquia específica
    # `on_delete=models.SET_NULL`: Si la parroquia asociada es eliminada, el campo de parroquia en el barrio se establecerá a `null`
    parroquia = models.ForeignKey(Parroquia, on_delete=models.SET_NULL, null=True)

    # Método para representar el objeto BarrioCiudadela como una cadena de texto
    def __str__(self):
        # Devuelve una representación concatenada del nombre del barrio, 
        # número de viviendas, parques, edificios residenciales y el nombre de la parroquia asociada
        return "%s %d %d %d %s" % (
            self.nombre,
            self.numero_viviendas,
            self.numero_parques,
            self.numero_edificios_residenciales,
            self.parroquia.nombre if self.parroquia else "Sin parroquia"  # Si no tiene parroquia, muestra "Sin parroquia"
        )
