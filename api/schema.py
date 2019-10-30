import graphene
from graphene_django.types import DjangoObjectType
import graphql_jwt

import users.schema
from .models import Prestamo, Sombrilla
from django.contrib.auth.models import User

class PrestamoType(DjangoObjectType):
    """Tipo de dato para manejar el tipo Prestamo"""

    class Meta:
        # Se relaciona con el origen de la data en models.Prestamo
        model = Prestamo


class SombrillaType(DjangoObjectType):
    """Tipo de dato para manejar el tipo Sombrilla"""
    class Meta:

        model = Sombrilla


class Query(users.schema.Query, graphene.ObjectType):
    """ Definición de las respuestas a las consultas posibles """

    # Se definen los posibles campos en las consultas

    prestamos = graphene.List(PrestamoType)

    sombrillas = graphene.List(SombrillaType)

    prestamo = graphene.Field(PrestamoType, 
                            id=graphene.Int(), 
                            usuario=graphene.Int(), 
                            sombrilla=graphene.Int(),
                            )

    sombrilla= graphene.Field(SombrillaType, 
                            id=graphene.Int(),
                            latitude=graphene.Float(),
                            longitude=graphene.Float(),
                            )

    # Se define las respuestas para cada campo definido
    def resolve_prestamos(self, info, **kwargs):
        # Responde con la lista de todos registros
        return Prestamo.objects.all()

    def resolve_sombrillas(self, info, **kwargs):

        return Sombrilla.objects.all()

    def resolve_prestamo(self, info, **kwargs):
        # Para filtrar en la tabla Prestamo
        id = kwargs.get('id')
        usuario = kwargs.get('usuario')
        sombrilla = kwargs.get('sombrilla')

        try:
            if id is not None:
                return Prestamo.objects.get(pk=id)
            if usuario is not None:
                return Prestamo.objects.get(usuario=usuario)
            if sombrilla is not None:
                return Prestamo.objects.get(sombrilla=sombrilla)
        except Prestamo.DoesNotExist:
            return None

    def resolve_sombrilla(self, info, **kwargs):

        id = kwargs.get('id')
        longitude = kwargs.get('longitude')
        latitude = kwargs.get('latitude')

        try:
            if id is not None:
                return Sombrilla.objects.get(pk=id)
            if longitude is not None:
                return Sombrilla.objects.get(longitude=longitude)
            if latitude is not None:
                return Sombrilla.objects.get(latitude=latitude)
        except Sombrilla.DoesNotExist:
            return None


class CrearPrestamo(graphene.Mutation):
    """
    Crea un prestamo en la tabla Prestamo
    """
    class Arguments:
        usuario = graphene.Int(required=True)
        sombrilla = graphene.Int(required=True)
        estatus = graphene.String(required=True)
    
    respuesta = graphene.Int()
    mensaje = graphene.String()

    def mutate(self, info, usuario, sombrilla, estatus):
        
        prestamo = Prestamo(
            usuario=User.objects.get(pk=usuario),
            sombrilla=Sombrilla.objects.get(pk=sombrilla),
            estatus=estatus
        )
        prestamo.save()
        respuesta=prestamo.id
        mensaje='Se inicio el prestamo' if estatus == 'I' else 'Se termino el prestamo'

        return CrearPrestamo(respuesta=respuesta, mensaje=mensaje)


class EliminarPrestamo(graphene.Mutation):
    """
    Elimina un prestamo de la tabla Prestamo
    """
    class Arguments:
        id = graphene.Int(required=True)
    
    respuesta = graphene.Boolean()
    mensaje = graphene.String()

    def mutate(self, info, id):
        
        try:
            validar = Prestamo.objects.get(pk=id)
            validar.delete()
            respuesta = True
            mensaje='Se elimino el prestamo'

        except Prestamo.DoesNotExist:
            respuesta = False
            mensaje = 'No existe el prestamo'

        return EliminarPrestamo(respuesta=respuesta, mensaje=mensaje)


class ActualizarPrestamo(graphene.Mutation):
    """
    Actualiza un Prestamo
    """
    class Arguments:
        id = graphene.Int(required=True)
        usuairo = graphene.Int()
        sombrilla = graphene.Int()

    respuesta = graphene.Boolean()
    mensaje = graphene.String()

    def mutate(self, info, id, usuario=None, sombrilla=None):

        try:
            prestamo = Prestamo.objects.get(pk=id)

            if usuario is not None:
                prestamo.usuario = usuario
            if sombrilla is not None:
                prestamo.sombrilla = sombrilla

            prestamo.save()

            respuesta = True
            mensaje = 'El prestamo fue actualizado'
        except Prestamo.DoesNotExist:
            respuesta = False
            mensaje ='No existe el prestamo'

        return ActualizarPrestamo(respuesta=respuesta, mensaje=mensaje)


class CrearSombrilla(graphene.Mutation):
    """
    Crea la ubicacion de una sombrilla
    """
    class Arguments:
        latitude = graphene.Float()
        longitude = graphene.Float()

    respuesta = graphene.Int()
    mensaje = graphene.String()

    def mutate(self, info,latitude, longitude): 
        # return CrearSombrilla(mensaje=str(latitude), respuesta=Decimal(latitude))

        sombrilla = Sombrilla(
            latitude=latitude,
            longitude=longitude,
        )

        sombrilla.save()

        respuesta= sombrilla.id
        mensaje = 'Se creo la sombrilla'

        return CrearSombrilla(respuesta=respuesta, mensaje=mensaje)


class ActualizarSombrilla(graphene.Mutation):
    """
    Actuliza la posicion y estatus de una sombrilla
    """
    class Arguments:
        id = graphene.Int()
        longitude=graphene.Float()
        latitude = graphene.Float()

    respuesta = graphene.Boolean()
    mensaje = graphene.String()

    def mutate(self, info, id, longitude, latitude):

        try:
            sombrilla = Sombrilla.objects.get(pk=id)
            if longitude is not None:
                sombrilla.longitude = longitude
            if latitude is not None:
                sobrilla.latitude = latitude
            sombrilla.save()
            respuesta = True
            mensaje = 'Sombrilla actualizada'
        except Sombrilla.DoesNotExist:
            respuesta = False
            mensaje = 'No existe la sombrilla'
        
        return ActualizarSombrilla(respuesta=respuesta, mensaje=mensaje)
    

class EliminarSombrilla(graphene.Mutation):
    """
    Elimina una sombrilla de la tabla Sombrilla
    """
    class Arguments:
        id = graphene.Int(required=True)

    respuesta = graphene.Boolean()
    mensaje = graphene.String()

    def mutate(self, info, id):

        try:
            sombrilla = Sombrilla.objects.get(pk=id)
            sombrilla.delete()
            
            respuesta = True
            mensaje = 'Sombrilla eliminada'

        except Sombrilla.DoesNotExist:
            respuesta = False
            mensaje = 'No existe la Sombrilla'        
        return EliminarSombrilla(respuesta=respuesta, mensaje=mensaje)


class Mutaciones(users.schema.Mutation, graphene.ObjectType):
    CrearPrestamo = CrearPrestamo.Field()
    ActualizarPrestamo = ActualizarPrestamo.Field()
    EliminarPrestamo = EliminarPrestamo.Field()
    CreaSombrilla = CrearSombrilla.Field()
    ActualizarSombrilla = ActualizarSombrilla.Field()
    EliminarSombrilla = EliminarSombrilla.Field()

    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


# Se crea un esquema que hace uso de la clase Query
schema = graphene.Schema(query=Query, mutation=Mutaciones)
