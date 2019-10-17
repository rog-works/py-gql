import sys

sys.path.append('/opt/app/vendor')

from collections import OrderedDict
from graphene import ObjectType, String, Int, Schema

# models/model.py

class Model(object):
	@classmethod
	def post(path: str, params: dict, auth: dict) -> OrderedDict:
		return OrderedDict({
			'id': 'id',
			'type': 'type',
			'stat': 1,
			'name': 'name',
		})

# schema/device.py

class Device(ObjectType):
	id = String()
	type = String()
	stat = Int()
	name = String()

# graphql/schema.py

class Query(ObjectType):
	device = Device()

	def resolve_device(root, info, id, type):
		return Model.post('/api/device', {'id': id, 'type': type}, authorize=True)

schema = Schema(query=Query)

# main.py

if __name__ == '__main__':
	query = sys.argv[1]
	result = schema.execute(query)
	print(result.data)

"""
query {
  device(id: "id", type: "type") {
    id
    type
    stat
  }
}
"""

