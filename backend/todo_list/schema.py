import graphene
from graphene_django import DjangoObjectType

from backend.todo_list.models import Todo, Category


# С помощью graphene_django привязываем типы к моделям,
# что позволит ходить по всей вложенности базы данных как угодно,
# прямо из интерфейса GraphiQL.
# Однако будьте осторожны, связывание таблиц практически напрямую
# с фронтом может быть чревато при росте проекта. Думаю такой способ
# подходит преимущественно для небольших CRUD приложений.
class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category


class TodoNode(DjangoObjectType):
    class Meta:
        model = Todo


class Query(graphene.ObjectType):
    """ Описываем запросы и возвращаемые типы данных """
    todo_list = graphene.List(TodoNode)
    categories = graphene.List(CategoryNode)

    def resolve_todo_list(self, info):
        return Todo.objects.all().order_by('-id')

    def resolve_categories(self, info):
        return Category.objects.all()


class Mutation(graphene.ObjectType):
    """ В мутации описываем типы запросов (прошу прощения за каламбур),
    типы возвращаемых данных и типы принимаемых переменных
    """
    add_todo = graphene.Field(TodoNode,
                              title=graphene.String(required=True),
                              text=graphene.String(),
                              due_date=graphene.Date(required=True),
                              category=graphene.String(required=True))
    remove_todo = graphene.Field(graphene.Boolean, todo_id=graphene.ID())
    toggle_todo = graphene.Field(TodoNode, todo_id=graphene.ID())

    def resolve_add_todo(self, info, **kwargs):
        category, _ = Category.objects.get_or_create(name=kwargs.pop('category'))
        return Todo.objects.create(category=category, **kwargs)

    def resolve_remove_todo(self, info, todo_id):
        try:
            Todo.objects.get(id=todo_id).delete()
        except Todo.DoesNotExist:
            return False
        return True

    def resolve_toggle_todo(self, info, todo_id):
        todo = Todo.objects.get(id=todo_id)
        todo.done = not todo.done
        todo.save()
        return todo
