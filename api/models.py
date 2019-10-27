from django.db import models


class Usuario(models.Model):
    """ Define la tabla User """
    nombre = models.CharField(max_length=40)
    email = models.EmailField()
    clave = models.CharField(max_length=20)

    # fechaAlta = models.DateField()
    # ultimaSesion = models.DateField()

    # apellidos = models.CharField(max_length=80, null=True, blank=True)
    # fechaNacimiento = models.DateField(null=True, blank=True)
    # GENERO = [
    #     ("H", "Hombre"),
    #     ("M", "Mujer"),
    # ]
    # genero = models.CharField(max_length=1, choices=GENERO)
    # clave = models.CharField(max_length=40, null=True, blank=True)
    # tipo = models.CharField(max_length=45, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.nombre)

class Sombrilla(models.Model):
    """Define la tabla de Umbrella"""    
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return "{}".format(self.id)


class Prestamo(models.Model):
    """"Define la tabla de Prestamos"""
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    sombrilla = models.ForeignKey(Sombrilla, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now=True)

    ESTATUS = [
        ("I", "Inicio"),
        ("T", "Termino"),
    ]

    estatus = models.CharField(max_length=1, choices=ESTATUS)

    def __str__(self):
        return "{}".format(self.id)

