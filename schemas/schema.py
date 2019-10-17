import graphene


class Device(graphene.ObjectType):
    id = graphene.String()
    type = graphene.String()
    stat = graphene.Int()
    name = graphene.String()
