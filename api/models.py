from django.db import models


class User(models.Model):
    """ Define la tabla User """
    name = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=20)

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
        return "{} {}".format(self.nombre, self.apellidos)
# Create your models here.
