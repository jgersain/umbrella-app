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
    user = graphene.Field(UserType, id=graphene.Int(), email=graphene.String(), name=graphene.String())
    # Se definen los posibles campos en las consultas
    all_users = graphene.List(UserType)  # allUsers

    # Se define las respuestas para cada campo definido
    def resolve_all_users(self, info, **kwargs):
        # Responde con la lista de todos registros
        return User.objects.all()
    
    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')
        email = kwargs.get('email')
        name = kwargs.get('name')

        if id is not None:
            return User.objects.get(pk=id)
        if email is not None:
            return User.objects.get(email=email)
        if name is not None:
            return User.objects.get(name=name)
        
        return None

class CreateUser(graphene.Mutation):
    """ Permite realizar la operación de crear en la tabla User """

    class Arguments:
        """ Define los argumentos para crear una User """
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        confirmPassword = graphene.String(required=True)


    response = graphene.Boolean()

    def mutate(self, info, name, email, password, confirmPassword):
        """ Se encarga de crear el nuevo Usuario """
        if password == confirmPassword:
            user = User(
            name=name,
            email=email,
            password=password,
            )
            user.save()
            response = True
        else:
            response = False

        # False si las contraseñas son diferentes 
        # True su las contraseñas coinciden    
        return CreateUser(response=response)

class UpdateUser(graphene.Mutation):
    """ Permite realizar la operación de modificar en la tabla User """
    class Arguments:
        """ Define los argumentos para modificar un Usuario """
        id = graphene.ID(required=True)
        name = graphene.String()
        email = graphene.String()
        password = graphene.String()

    response = graphene.String()
    def mutate(self, info, id, name=None, email=None, password=None):
        """
        Se encarga de modificar el Usuario identificado por el id.
        """

        try:
            # Si existe se modifica
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
            response = "True"
        except User.DoesNotExist:
            response = "El usuario no existe"
        # Se regresa una instancia de esta mutación
        return UpdateUser(response=response)

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

        return DeleteUser(response=response)

class Mutations(graphene.ObjectType):
    createUser = CreateUser.Field()
    updateUser = UpdateUser.Field()
    deleteUser = DeleteUser.Field()


# Se crea un esquema que hace uso de la clase Query
schema = graphene.Schema(query=Query, mutation=Mutations)
