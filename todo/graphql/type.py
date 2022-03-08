from dataclasses import field

from graphene_django import DjangoObjectType
from todo.models import Todo
from users.models import CustomUser


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        field = '__all__'
        

class UserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        field = '__all__'



