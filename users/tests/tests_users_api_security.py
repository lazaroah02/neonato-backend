import json
from graphene_django.utils.testing import GraphQLTestCase
from django.contrib.auth import get_user_model
User = get_user_model()

class SecurityUserApiTests(GraphQLTestCase):
    def setUp(self):
            #creo un usuario admin
            admin = User.objects.create_superuser(username = "admin", email = "admin@gmail.com", password="92MzPEFi")
            #authenticacion como admin
            response1 = self.make_query(
            query =  '''
                mutation{
                    tokenAuth(username:"admin", password:"92MzPEFi"){
                        token,
                        errors,
                        success,
                    }
                }
                ''') 
            self.superuser_token = json.loads(response1.content)["data"]["tokenAuth"]["token"]

    