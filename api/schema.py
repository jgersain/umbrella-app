import graphene

from graphene_django.types import DjangoObjectType
from .models import Usuario, Prestamo, Sombrilla

class UsuarioType(DjangoObjectType):
    """ Tipo de dato para manejar el tipo Usuario """
    class Meta:
        # Se relaciona con el origen de la data en models.Usuario
        model = Usuario
        
class PrestamoType(DjangoObjectType):
    """Tipo de dato para manejar el tipo Prestamo"""

    class Meta:
        # Se relaciona con el origen de la data en models.Prestamo
        model = Prestamo

class SombrillaType(DjangoObjectType):
    """Tipo de dato para manejar el tipo Sombrilla"""
    class Meta:

        model = Sombrilla


class Query(graphene.ObjectType):
    """ Definición de las respuestas a las consultas posibles """

    # Se definen los posibles campos en las consultas
    usuarios = graphene.List(UsuarioType)  # allUsuarios

    prestamos = graphene.List(PrestamoType)

    sombrillas = graphene.List(SombrillaType)

    usuario = graphene.Field(UsuarioType, 
                            id=graphene.Int(), 
                            email=graphene.String(), 
                            nombre=graphene.String()
                            )

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
    def resolve_usuarios(self, info, **kwargs):
        # Responde con la lista de todos registros
        return Usuario.objects.all()
    
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
    
    def resolve_usuario(self, info, **kwargs):
        # Para filtrar en la tabla Usuario
        id = kwargs.get('id')
        email = kwargs.get('email')
        nombre = kwargs.get('nombre')

        try:
            if id is not None:
                return Usuario.objects.get(pk=id)
            if email is not None:
                return Usuario.objects.get(email=email)
            if nombre is not None:
                return Usuario.objects.get(nombre=nombre)    
        except Usuario.DoesNotExist:
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

class CrearUsuario(graphene.Mutation):
    """ 
    Crea un usuario en la tabla Usuario,
    valida que el correo no exista en BD
    y regresa ID de usuario
    """

    class Arguments:
        """ Define los argumentos para crear un usuario """
        nombre = graphene.String(required=True)
        email = graphene.String(required=True)
        clave = graphene.String(required=True)
        confirmarClave = graphene.String(required=True)
        
    # El atributo usado para la respuesta de la mutación
    #usuario = graphene.Field(UsuarioType)
    respuesta = graphene.Int()
    mensaje = graphene.String()

    def mutate(self, info, nombre, email, clave, confirmarClave):
        """ Se encarga de crear el nuevo Usuario """
        if clave == confirmarClave:
           
            try:
                verificarEmail = Usuario.objects.get(email=email)
                respuesta = None
                mensaje = 'Ya existe un usuario con este correo'
                return CrearUsuario(respuesta=respuesta, mensaje=mensaje)

            except Usuario.DoesNotExist:
                usuario = Usuario(
                nombre=nombre,
                email=email,
                clave=clave,
                )
            
            usuario.save()    
            respuesta = usuario.id
            mensaje = 'Usuario creado correctamente'
        return CrearUsuario(respuesta=respuesta, mensaje=mensaje)


class EliminarUsuario(graphene.Mutation):
    """ Elimina un usuario de la tabla Usuario """
    class Arguments:
        """ Define los argumentos para eliminar una Usuario """
        id = graphene.ID(required=True)

    # El atributo usado para la respuesta de la mutación, en este caso sólo se
    # indicará con la variuable ok true en caso de éxito o false en caso
    # contrario
    respuesta = graphene.Boolean()
    mensaje = graphene.String()

    def mutate(self, info, id):
        """ Se encarga de eliminar al Usuario """
        try:
            # Elimina al Usuario si existe
            usuario = Usuario.objects.get(pk=id)
            usuario.delete()
            respuesta = True
            mensaje = 'El usuario ha sido eliminado correctamente'
        except Usuario.DoesNotExist:
            # No existe el Usuario
            respuesta = False
            mensaje = 'El usuario no existe en la Base de Datos'
        # Se regresa una instancia de esta mutación
        return EliminarUsuario(respuesta=respuesta, mensaje=mensaje)


class ActualizarUsuario(graphene.Mutation):
    """ 
    Modifica usuario en la tabla Usuario
    verificando que no exista el correo en BD
    """
    class Arguments:
        """ Define los argumentos para modificar un Usuario """
        id = graphene.ID(required=True)
        nombre = graphene.String()
        email = graphene.String()
        clave = graphene.String()
    
    respuesta = graphene.Boolean()
    mensaje = graphene.String()
    

    def mutate(self, info, id, nombre=None, email=None, clave=None):
        """
        Modifica los valores en caso de haber sido enviados
        """
        try:
            usuario = Usuario.objects.get(pk=id)
                       # Si el Usuario existe
            if nombre is not None:
                usuario.nombre = nombre
            if clave is not None:
                usuario.clave = clave
            
            if email is not None:
                try:
                    verificarEmail = Usuario.objects.get(email=email)
                    respuesta = False
                    mensaje = 'Ya existe un usuario con este Email'
                except Usuario.DoesNotExist:
                    usuario.email = email

                    usuario.save()

                    respuesta = True
                    mensaje = 'El usuario fue actualizado correctamente'
 
        except Usuario.DoesNotExist:
            # Si el Usuario no existe
            respuesta = False
            mensaje = 'El usuario no existe en la Base de Datos'
            return ActualizarUsuario(respuesta=respuesta, mensaje=mensaje)
        
        # Se regresa una instancia de esta mutación
        return ActualizarUsuario(respuesta=respuesta, mensaje=mensaje)


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
            usuario=Usuario.objects.get(pk=usuario),
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
        latitude =  graphene.Float()
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


class Mutaciones(graphene.ObjectType):
    CrearUsuario = CrearUsuario.Field()
    ActualizarUsuario = ActualizarUsuario.Field()
    EliminarUsuario = EliminarUsuario.Field()
    CrearPrestamo = CrearPrestamo.Field()
    ActualizarPrestamo = ActualizarPrestamo.Field()
    EliminarPrestamo = EliminarPrestamo.Field()
    CreaSombrilla = CrearSombrilla.Field()
    ActualizarSombrilla = ActualizarSombrilla.Field()
    EliminarSombrilla = EliminarSombrilla.Field()


# Se crea un esquema que hace uso de la clase Query
schema = graphene.Schema(query=Query, mutation=Mutaciones)
