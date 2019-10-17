import graphene


class Device(graphene.ObjectType):
    id = graphene.String()
    kind = graphene.String()
    stat = graphene.Int()
    name = graphene.String()
