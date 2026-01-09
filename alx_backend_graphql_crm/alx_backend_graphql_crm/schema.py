import graphene
#from crm.schema import Query as CRMQuery, Mutation as CRMMutation

class Query(graphene.ObjectType):
    # Define a field named 'hello' that returns a String
    hello = graphene.String(default_value="Hello, GraphQL!")
    #return hello

# Create the schema instance to be used by the GraphQL view
schema = graphene.Schema(query=Query)