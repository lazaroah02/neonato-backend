import graphene
from graphql_auth.schema import UserQuery, MeQuery
from graphql_auth import mutations

class Query(UserQuery, MeQuery, graphene.ObjectType):
    pass

class AuthMutation(graphene.ObjectType) :
    verify_account = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    password_change = mutations.PasswordChange.Field()
    
class Mutation(AuthMutation, graphene.ObjectType):
    pass