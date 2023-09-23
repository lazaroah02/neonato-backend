from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model
from utils.validators import validate_password
from django.contrib.auth.hashers import make_password
from django.core.validators import EmailValidator
from utils.verify_user import verify_user
from django_graphene_permissions import permissions_checker
from utils.custom_permissions import IsStaff, CustomIsAuthenticated
from utils.convert_graphql_id_to_int import convert_graphql_id_to_int
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
        is_staff = graphene.Boolean()
    user = graphene.Field(UserType) 
    
    @permissions_checker([CustomIsAuthenticated, IsStaff])
    def mutate(self, info, username, password, email, is_staff = False):
        validate_password(password)
        EmailValidator()(email)
        hash_password = make_password(password)
        user = CustomUser(username = username, password = hash_password, email = email, is_staff = is_staff)
        user.save()
        verify_user(username)
        return CreateUser(user)

class DeleteUser(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    message = graphene.String()   
    
    @permissions_checker([CustomIsAuthenticated, IsStaff])
    def mutate(self, info, id):
        num_id = convert_graphql_id_to_int(id)
        user = CustomUser.objects.get(id = num_id)   
        user.delete()
        return DeleteUser("User deleted succesfully")  

class UpdateUser(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        username = graphene.String() 
        email = graphene.String()  
        is_staff = graphene.Boolean()  
        is_active = graphene.Boolean() 
    user = graphene.Field(UserType)    
    
    @permissions_checker([CustomIsAuthenticated, IsStaff])
    def mutate(self, info, id, **kwargs):
        num_id = convert_graphql_id_to_int(id)
        user = CustomUser.objects.get(id = num_id)
        user.username = kwargs.get("username", user.username)
        user.email = kwargs.get('email', user.email)
        user.is_staff = kwargs.get('is_staff', user.is_staff)
        user.is_active = kwargs.get("is_active", user.is_active)
        user.save()
        return UpdateUser(user)
    
class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()    
    delete_user = DeleteUser.Field()
    update_user = UpdateUser.Field()
                 