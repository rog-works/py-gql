import sys
import bootstrap
import graphene
from gql.query import Query


if __name__ == '__main__':
    bootstrap.started()
    query = sys.argv[1]
    schema = graphene.Schema(query=Query)
    result = schema.execute(query)
    print(result.data)

"""
# examples
query {
  device(id: "id", kind: "kind") {
    id
    kind
    stat
  }
}
"""
