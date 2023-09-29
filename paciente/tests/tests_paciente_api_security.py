import json
from graphene_django.utils.testing import GraphQLTestCase
from django.contrib.auth import get_user_model
User = get_user_model()

class SecurityPacienteApiTests(GraphQLTestCase):    
    def make_query(self, query, token = ""):
        response = self.query(
            query = query,
            headers={
                "HTTP_AUTHORIZATION":f"JWT {token}"
                }
        )   
        return response                
     
    def setUp(self):
        #creo un usuario admin
        admin = User.objects.create_superuser(username = "admin", email = "admin@gmail.com", password="92MzPEFi")
        #creo un usuario normal
        user = User.objects.create_user(username = "testuser", email = "testuser@gmail.com", password="92MzPEFi")
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
        #authenticacion como user normal
        response2 = self.make_query(
           query =  '''
            mutation{
                tokenAuth(username:"testuser", password:"92MzPEFi"){
                    token,
                    errors,
                    success,
                }
            }
            ''') 
        self.user_token = json.loads(response2.content)["data"]["tokenAuth"]["token"]
    
    def test_get_pacientes_without_authenticated_user(self):
        query = '''
        {
            pacientes{
                edges{
                    node{
                        id,
                        nombre
                    }
                }
            }
        }
        '''
        response = self.make_query(query=query)
        self.assertContains(response = response,text = "You must be authenticated to do this operation")
    
    def test_get_paciente_without_authenticated_user(self):
        query = '''
        {
            paciente(id:""){
                id,
                nombre
            }
        }
        '''
        response = self.make_query(query=query)
        self.assertContains(response = response, text = "You must be authenticated to do this operation")    
    
    def test_create_paciente_without_authenticated_user(self):
        query = '''
           mutation {
            createPaciente(
                fecha:"2023-09-06",
            ){
                paciente{
                id, 
                }
            }
            }
        '''
        response = self.make_query(query=query)
        self.assertContains(response = response, text = "You must be authenticated to do this operation")  
    
    def test_update_paciente_without_authenticated_user(self):
        query = '''
           mutation {
            createPaciente(
                fecha:"2023-09-06",
            ){
                paciente{
                id, 
                }
            }
            }
        '''
        response = self.make_query(query=query)
        self.assertContains(response = response, text = "You must be authenticated to do this operation")      
    
    def test_create_paciente_without_being_admin(self):
        query = '''
           mutation {
            createPaciente(
                fecha:"2023-09-06",
            ){
                paciente{
                id, 
                }
            }
            }
        '''
        response = self.make_query(query=query, token = self.user_token)
        self.assertContains(response = response, text = "You must be a staff member to do this operation")          
    
    def test_update_paciente_without_being_admin(self):
        query = '''
           mutation {
            updatePaciente(
                id:"",
            ){
                paciente{
                id, 
                }
            }
            }
        '''
        response = self.make_query(query=query, token = self.user_token)
        self.assertContains(response = response, text = "You must be a staff member to do this operation")     
    
    def test_delete_paciente_without_being_admin(self):
        query = '''
           mutation {
            deletePaciente(
                id:"",
            ){
                message
            }
            }
        '''
        response = self.make_query(query=query, token = self.user_token)
        self.assertContains(response = response, text = "You must be a staff member to do this operation")  
    
    def test_delete_paciente_without_being_authenticated(self):
        query = '''
           mutation {
            deletePaciente(
                id:"",
            ){
                message
            }
            }
        '''
        response = self.make_query(query=query)
        self.assertContains(response = response, text = "You must be authenticated to do this operation")    
    