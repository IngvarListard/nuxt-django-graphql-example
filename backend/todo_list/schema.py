import graphene
from graphene_django import DjangoObjectType

from backend.todo_list.models import Todo, Category


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category


class TodoNode(DjangoObjectType):
    class Meta:
        model = Todo


class Query(graphene.ObjectType):
    todo_list = graphene.List(TodoNode)
    categories = graphene.List(CategoryNode)

    def resolve_todo_list(self, info):
        """ Получение всего списка записей Todo """
        return Todo.objects.all()

    def resolve_categories(self, info):
        """ Получение всего списка записей Category """
        return Category.objects.all()


class AddTodo(graphene.Mutation):
    todo = graphene.Field(TodoNode)

    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String()
        due_date = graphene.Date(required=True)
        category = graphene.String(required=True)

    def mutate(self, info, **kwargs):
        category, _ = Category.objects.get_or_create(name=kwargs.pop('category'))
        new_todo = Todo.objects.create(category=category, **kwargs)
        return AddTodo(todo=new_todo)


class Mutation(graphene.ObjectType):
    add_todo = AddTodo.Field()
