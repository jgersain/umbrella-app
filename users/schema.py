from django.contrib.auth import get_user_model

import graphene
from graphene_django import DjangoObjectType
import graphql_jwt


class UserType(DjangoObjectType):
  class Meta:
    model = get_user_model()


class CreateUser(graphql_jwt.JSONWebTokenMutation, graphene.Mutation):
  user = graphene.Field(UserType)

  class Arguments:
    username = graphene.String(required=True)
    password = graphene.String(required=True)
    email = graphene.String(required=True)

  def mutate(self, info, username, password, email):
    user = get_user_model()(
      username=username,
      email=email
    )
    user.set_password(password)
    user.save()

    return CreateUser(user=user)

  @classmethod
  def resolve(cls, root, info, **kwargs):
    return cls(user=info.context.user)
    

class UpdateUser(graphene.Mutation):
    class Arguments:        
        id = graphene.ID(required=True)
        username = graphene.String()
        email = graphene.String()
        password = graphene.String()
    
    respuesta = graphene.Boolean()
    mensaje = graphene.String()
    
    def mutate(self, info, id, username=None, email=None, password=None):
        try:
            user = get_user_model().objects.get(pk=id)
                       # Si el Usuario existe
            if username is not None:
                user.username = username
            if password is not None:
                user.password = password
            
            if email is not None:
                try:
                    userEmail = get_user_model().objects.get(email=email)
                    respuesta = False
                    mensaje = 'Ya existe un usuario con este Email'
                except get_user_model().DoesNotExist:
                    user.email = email

                    user.save()

                    respuesta = True
                    mensaje = 'El usuario fue actualizado correctamente'
 
        except get_user_model().DoesNotExist:
            # Si el Usuario no existe
            respuesta = False
            mensaje = 'El usuario no existe en la Base de Datos'

        return UpdateUser(respuesta=respuesta, mensaje=mensaje)


class DeleteUser(graphene.Mutation):

  class Arguments:
    id = graphene.Int(required=True)

  respuesta = graphene.Boolean()
  mensaje = graphene.String()
  
  def mutate(self, info, id):

    user = get_user_model().objects.get(pk=id)
    user.delete()

    return UpdateUser(respuesta=True, mensaje="Eliminado")


class Mutation(graphene.ObjectType):
  create_user = CreateUser.Field()
  update_user = UpdateUser.Field()
  delete_user = DeleteUser.Field()


class Query(graphene.ObjectType):
  me = graphene.Field(UserType)
  users = graphene.List(UserType)
  user = graphene.Field(UserType, id=graphene.Int(),username=graphene.String(), email=graphene.String(), password=graphene.String())

  def resolve_users(self, info):
    return get_user_model().objects.all()

  def resolve_user(self, info, **kwargs):

        id = kwargs.get('id')
        email = kwargs.get('email')
        username = kwargs.get('username')
        password = kwargs.get('password')

        try:
            if id is not None:
                return get_user_model().objects.get(pk=id)
            if email is not None:
                return get_user_model().objects.get(email=email)
            if username is not None:
                return get_user_model().objects.get(username=username)   
            if password is not None:
                return get_user_model().objects.get(password=password) 
        except get_user_model().DoesNotExist:
            return None


  def resolve_me(self, info):
    user = info.context.user
    if user.is_anonymous:
      raise Exception('Not loggen in!')

    return user