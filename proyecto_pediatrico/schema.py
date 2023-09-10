import graphene
import paciente.schema

class Query(paciente.schema.Query, graphene.ObjectType):
    pass

class Mutation(paciente.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation = Mutation)