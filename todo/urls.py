from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from todo.graphql.query import schema
from django.contrib.auth.mixins import LoginRequiredMixin

class PrivateGraphQLView(LoginRequiredMixin, GraphQLView):
    pass

urlpatterns = [
    path("", csrf_exempt(PrivateGraphQLView.as_view(graphiql=True, schema=schema))),
]