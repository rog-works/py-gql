import graphene
from schemas.schema import Device
from models.model import Model


class Query(graphene.ObjectType):
    device = graphene.Field(Device)

    def resolve_device(root, info, id, type):
        return Model.post(
            f'/api/device/{id}',
            {'type': type},
            authorize=True
        )
