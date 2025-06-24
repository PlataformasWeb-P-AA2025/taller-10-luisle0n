from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_inicial, name='vista_inicial'),  # Página principal con enlaces
    path('barrios/', views.lista_barrios, name='lista_barrios'),
    path('crear/barrio/', views.crear_barrio, name='crear_barrio'),
    path('parroquias/', views.lista_parroquias_y_barrios, name='lista_parroquias'),
    path('crear/parroquia/', views.crear_parroquia, name='crear_parroquia'),
]
