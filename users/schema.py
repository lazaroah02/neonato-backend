from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model
from .validators import validate_password
from django.contrib.auth.hashers import make_password
from django.core.validators import EmailValidator
import graphene
CustomUser = get_user_model()


class UserType(DjangoObjectType):
    class Meta:
        model = CustomUser

class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String()
        password = graphene.String()
        email = graphene.String()  
    user = graphene.Field(UserType) 
    
    def mutate(self, info, username, password, email):
        validate_password(password)
        EmailValidator()(email)
        hash_password = make_password(password)
        user = CustomUser(username = username, password = hash_password, email = email)
        user.save()
        return CreateUser(user)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()    
                 