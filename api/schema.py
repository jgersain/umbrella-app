import graphene

from graphene_django.types import DjangoObjectType
from .models import User


class UserType(DjangoObjectType):
    """ Tipo de dato para manejar el tipo User """
    class Meta:
        # Se relaciona con el origen de la data en models.User
        model = User
    

class Query(graphene.ObjectType):
    """ Definición de las respuestas a las consultas posibles """

    # Se definen los posibles campos en las consultas
    all_users = graphene.List(UserType)  # allUsers

    # Se define las respuestas para cada campo definido
    def resolve_all_users(self, info, **kwargs):
        # Responde con la lista de todos registros
        return User.objects.all()

class CreateUser(graphene.Mutation):
    """ Permite realizar la operación de crear en la tabla User """

    class Arguments:
        """ Define los argumentos para crear una User """
        name = graphene.String(required=True)
        email = graphene.String()
        password = graphene.String()
        confirmPassword = graphene.String()
        
    # El atributo usado para la respuesta de la mutación
    user = graphene.Field(UserType)

    def mutate(self, info, name, email, password, confirmPassword):
        """ Se encarga de crear el nuevo Usuario """
        if password == confirmPassword:
            user = User(
            name=name,
            email=email,
            password=password,
            )
            user.save()

        return CreateUser(user=user)


class DeleteUser(graphene.Mutation):
    """ Permite realizar la operación de eliminar en la tabla User """
    class Arguments:
        """ Define los argumentos para eliminar una User """
        id = graphene.ID(required=True)

    # El atributo usado para la respuesta de la mutación, en este caso sólo se
    # indicará con la variuable ok true en caso de éxito o false en caso
    # contrario
    response = graphene.Boolean()

    def mutate(self, info, id):
        """ Se encarga de eliminar al Usuario """
        try:
            # Elimina al Usuario si existe
            user = User.objects.get(pk=id)
            user.delete()
            response = True
        except User.DoesNotExist:
            # No existe el Usuario
            response = False
        # Se regresa una instancia de esta mutación
        return DeleteUser(response=response)


class UpdateUser(graphene.Mutation):
    """ Permite realizar la operación de modificar en la tabla User """
    class Arguments:
        """ Define los argumentos para modificar un Usuario """
        id = graphene.ID(required=True)
        name = graphene.String()
        email = graphene.String()
        password = graphene.String()
    # El campo regresado como respuesta de la mutación, en este caso se regres el modificada.
    user = graphene.Field(UserType)

    def mutate(self, info, id, name=None, email=None, password=None):
        """
        Se encarga de modificar la Zona identificada por el id.
        """
        try:
            # Si la zona existe se modifica
            user = User.objects.get(pk=id)
            # Si algunos de los atributos es proporcionado, entonces se
            # actualiza
            if name is not None:
              user.name = name
            if email is not None:
              user.email = email
            if password is not None:
              user.password = password
            user.save()
        except user.DoesNotExist:
            # Si el Usuario no existe, se procesa la excepción
            user = None
        # Se regresa una instancia de esta mutación
        return UpdateUser(user=user)


class Mutaciones(graphene.ObjectType):
    createUser = CreateUser.Field()
    updateUser = UpdateUser.Field()
    deleteUser = DeleteUser.Field()


# Se crea un esquema que hace uso de la clase Query
schema = graphene.Schema(query=Query, mutation=Mutaciones)
