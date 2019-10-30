from django.db import models
from django.contrib.auth.models import User

class Sombrilla(models.Model):
    """Define la tabla de Umbrella"""    
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return "{}".format(self.id)


class Prestamo(models.Model):
    """"Define la tabla de Prestamos"""
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    sombrilla = models.ForeignKey(Sombrilla, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now=True)

    ESTATUS = [
        ("I", "Inicio"),
        ("T", "Termino"),
    ]

    estatus = models.CharField(max_length=1, choices=ESTATUS)

    def __str__(self):
        return "{}".format(self.id)

