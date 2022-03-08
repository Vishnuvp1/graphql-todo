from django.test import TestCase
from graphene_django.utils.testing import GraphQLTestCase
import json
from todo.graphql.query import schema 
from graphene.test import Client

# Create your tests here.


# class TodoTestCase(GraphQLTestCase):

#     def sent_todo(self, title, content, due_date):

#         query = """
#         mutation createTodo($title :String!, $content :String!, $due_date :String!){
#             createTodo(title:$title, content:$content, due_date:$due_date){
#                 ok
#                 message
#                 }
#             }

#         """
#         result = self.query(query, variables={
#             'title': title, 'content': content, 'due_date': due_date
#         }, headers={
#             'Content-Type': 'application/json',
#         })
#         print(result, '---------')
#         print(result.content, '------')
#         return result

#     def test_sample(self):
#         print('----------++++--------')
#         result = self.sent_todo(
#             'sample', 'sample', '2022-10-10'
#         )
#         assert result['errors'][0]['message'] == "This is a sample message"


todo_list_query = '''
    query {
    todo{
        id
        title
        content
        dueDate
    }
    }
'''

create_todo_mutation = '''
    mutation CreateTodo (
        $title : String!
        $content : String!
        $due_date : Date!
    ){
    createTodo (
        title : $title,
        content : $content, 
        dueDate : $due_date
        ){
        todo {
        title
        content
        dueDate 
        }
    }
    }
'''


update_todo_mutation = '''
    mutation CreateTodo (
        $id : ID!,
        $title : String!,
        $content : String!,
        $due_date : Date!,
    ){
    createTodo (
        id : $id
        title : $title,
        content : $content, 
        dueDate : $due_date
        ){
        todo {
        title
        content
        dueDate 
        }
    }
    }
'''


class TestTodo(TestCase):

    def setUp(self):
        self.client = Client(schema)
        
    def test_create_todo(self):
        print('-----$$$-----')
        payload = {
            "title" : "new",
            "content" : "new",
            "due_date" : "2022-10-10"
        }

        response = self.client.execute(create_todo_mutation, variables = {**payload})
        response_todo = response.get("data").get("createTodo").get("todo")
        print(response_todo)

        # title = response_todo.get("title")
        # assert title == payload["title"]