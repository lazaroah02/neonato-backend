import graphene
import paciente.schema
import authentication.schema
import users.schema
import graphics.schema

class Query(paciente.schema.Query, authentication.schema.Query, graphics.schema.Query, graphene.ObjectType):
    pass

class Mutation(paciente.schema.Mutation,  authentication.schema.Mutation, users.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation = Mutation)