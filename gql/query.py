import graphene
from schemas.schema import Device
from models.model import Model


class Query(graphene.ObjectType):
    device = graphene.Field(
        Device,
        id=graphene.String(),
        kind=graphene.String()
    )

    def resolve_device(root, info, id, kind):
        return Model.post(
            f'/api/device/1',
            {'kind': 'tv'}
        )
