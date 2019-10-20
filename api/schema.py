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
    Users = graphene.List(UserType)  # allUsers

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
        """
        Se encarga de crear el nuevo Usuario.
        """
        if password == confirmPassword:
            user = User(
            nombre=nombre,
            email=email,
            password=password,
            )
            user.save()

        return CreateUser(user=user)


class Mutaciones(graphene.ObjectType):
    createUser = CreateUser.Field()


# Se crea un esquema que hace uso de la clase Query
schema = graphene.Schema(query=Query, mutation=Mutaciones)


