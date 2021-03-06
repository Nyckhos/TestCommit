from django.db import models
from django.db.models.fields import EmailField
from django.db.models.manager import ManagerDescriptor

# Create your models here.

COLOR_CHOICES = (
    ('green','GREEN'),
    ('blue', 'BLUE'),
    ('red','RED'),
    ('orange','ORANGE'),
    ('black','BLACK'),
)



class Persona(models.Model): 
    nombre = models.TextField(max_length=30)
    apellido = models.TextField(max_length=30)
    email = models.TextField(max_length=15)
    celular = models.TextField(max_length=50)
    usuario = models.TextField(max_length=300)
    region = models.CharField(max_length=6, choices=COLOR_CHOICES, default='green')
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


    
