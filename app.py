import sys

sys.path.append('/opt/app/vendor')

from graphene import ObjectType, String, Schema

class Query(ObjectType):
    hello = String(name=String(default_value="hoge"))
    goodbye = String()

    def resolve_hello(root, info, name):
        return name

    def resolve_goodbye(root, info):
        return 'fuga'

schema = Schema(query=Query)

if __name__ == '__main__':
	result = schema.execute(sys.argv[1])
	print(result.data)


