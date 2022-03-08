import graphene
from .type import TodoType, UserType
from todo.models import Todo


class Query(graphene.ObjectType):

    todo = graphene.List(TodoType)
    single_todo = graphene.Field(TodoType, id=graphene.Int(), title=graphene.String())

    def resolve_todo(root, info):
        user=info.context.user
        return Todo.objects.filter(owner=user)

    def resolve_single_todo(self, info, **kwargs):
        id = kwargs.get('id')
        title = kwargs.get('title')

        if id is not None:
            return Todo.objects.get(pk=id)

        if title is not None:
            return Todo.objects.get(title=title)

        return None


class CreateTodo(graphene.Mutation):

    class Arguments:
        title = graphene.String(required=True)
        content = graphene.String(required=True)
        due_date = graphene.Date(required=True)

    todo = graphene.Field(TodoType)

    @classmethod
    def mutate(cls, root, info, title, content, due_date):
        owner = info.context.user
        todo = Todo(title=title, content=content, due_date=due_date, owner=owner)
        todo.save()
        return CreateTodo(todo=todo)


class UpdateTodo(graphene.Mutation):

    class Arguments:
        id = graphene.ID()
        title = graphene.String(required=True)
        content = graphene.String(required=True)
        due_date = graphene.Date(required=True)

    todo = graphene.Field(TodoType)

    @classmethod
    def mutate(cls, root, info, id,  title, content, due_date):
        todo = Todo.objects.get(id=id)
        owner = info.context.user
        todo.owner = owner
        todo.title = title
        todo.content = content
        todo.due_date = due_date
        todo.save()
        return UpdateTodo(todo=todo)

class Mutation(graphene.ObjectType):
    create_todo = CreateTodo.Field()
    update_todo = UpdateTodo.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)