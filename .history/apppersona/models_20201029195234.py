from django.db import models
from django.db.models.fields import EmailField
from django.db.models.manager import ManagerDescriptor

# Create your models here.

REGIONES = (

    ('primera' ,'I Región de Tarapacá'),
    ('segunda','II Región de Antofagasta'),
    ('tercera','III Región de Atacama'),
    ('cuarta','IV Región de Coquimbo'),
    ('quinta','V Región de Valparaíso'),
    ('sexta','VI Región del Libertador General Bernardo O’Higgins'),
    ('septima','VII Región del Maule'),
    ('octava','VIII Región del Biobío'),
    ('novena','IX Región de La Araucanía'),
    ('decima','X Región de Los Lagos'),
    ('decimoprimera','XI Región Aysén del General Carlos Ibáñez del Campo'),
    ('decimosegunda','XII Región de Magallanes y Antártica Chilena'),
    ('rm','Región Metropolitana de Santiago'),
    ('decimocuarta','XIV Región de Los Ríos'),
    ('decimoquinta','XV Región de Arica y Parinacota'),
    ('decimosexta','XVI Región de Ñuble')
)





class Persona(models.Model): 
    nombre = models.TextField(max_length=30)
    apellido = models.TextField(max_length=30)
    email = models.TextField(max_length=15)
    celular = models.TextField(max_length=50)
    usuario = models.TextField(max_length=300)
    region = models.CharField(max_length=6, choices=REGIONES, default='rm')
    contraseña = models.TextField(max_length=30)
    contraseñaconfirmar = models.TextField(max_length=30)
    
    def __str__(self):
        return self.nombre + " " + self.email 

class TarjetaJunaeb(models.Model):
    numeroTarjeta = models.TextField(max_length=12) # es un identificador
    montoDisponible = models.IntegerField()
    rut = models.TextField(max_length=9)
    clave = models.TextField(max_length=8)

    def __str__(self):
        return self.rut + " " + self.numeroTarjeta 


    
