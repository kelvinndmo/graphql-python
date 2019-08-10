import graphene
from graphene_django import DjangoObjectType
from .models import Property


class PropertyType(DjangoObjectType):
    class Meta:
        model = Property


class Query(graphene.ObjectType):
    properties = graphene.List(PropertyType)

    def resolve_properties(self, info, *kwargs):
        return Property.objects.all()


# lets now create our properties
class CreateProperty(graphene.Mutation):
    name = graphene.String()
    description = graphene.String()
    location = graphene.String()

    class Arguments:
        name = graphene.String()
        description = graphene.String()
        location = graphene.String()

    def mutate(self, info, name, description, location):
        property = Property(
            name=name, description=description, location=location)
        property.save()

        return CreateProperty(
            name=property.name,
            description=property.description,
            location=property.location
        )


class Mutation(graphene.ObjectType):
    create_property = CreateProperty.Field()
