import graphene
from backend.todo_list.schema import Query, Mutation
schema = graphene.Schema(query=Query, mutation=Mutation)
