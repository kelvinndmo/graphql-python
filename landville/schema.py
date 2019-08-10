import graphene
import property.schema


class Query(property.schema.Query, graphene.ObjectType):
    pass


class Mutation(property.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
