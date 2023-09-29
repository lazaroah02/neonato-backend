import json
from graphene_django.utils.testing import GraphQLTestCase
from django.contrib.auth import get_user_model
User = get_user_model()

class pacienteApiTests(GraphQLTestCase):
    def make_query(self, query, token = ""):
        response = self.query(
            query = query,
            headers={
                "HTTP_AUTHORIZATION":f"JWT {token}"
                }
        )   
        return response  
    
    def create_paciente(self):
        query = '''
           mutation {
            createPaciente(
                fecha: "2023-09-09",
                nombre: "paciente_test",
                nombreDeLaMadre: "Juana",
                provincia: "Holguin",
                municipio: "Holguin",
                diagnosticoEgreso: "Bien",
                direccion: "Calle 1",
                alta: VIVO,
            ){
                paciente{
                    id,
                }
            }
            }
        '''
        response = self.make_query(query=query, token = self.superuser_token)
        content = json.loads(response.content)
        return content["data"]["createPaciente"]["paciente"]["id"]
    
    def get_paciente(self, paciente_id, token):
        query = '''query paciente($id:ID!){
                paciente(id:$id){
                    id,
                }
            }'''
        response = self.query(
            query = query,
            headers={
                "HTTP_AUTHORIZATION":f"JWT {token}"
                },
            variables = {
                "id":paciente_id
            }
        )  
        return response
    
    def delete_paciente(self, paciente_id):
        query = '''
            mutation deletePaciente($id:ID!){
                deletePaciente(id:$id){
                    message
                }
            }
            
        '''        
        response = self.query(
            query = query,
            headers = {
                "HTTP_AUTHORIZATION":f"JWT {self.superuser_token}",
            },
            variables = {
                "id":paciente_id,
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
    
    def test_get_pacientes_with_normal_users(self):
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
        response = self.make_query(query=query, token = self.user_token)
        content = json.loads(response.content)
        self.assertListEqual(content["data"]["pacientes"]["edges"], [])
    
    def test_get_pacientes_with_admin_users(self):    
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
        response = self.make_query(query=query, token = self.superuser_token)
        content = json.loads(response.content)
        self.assertListEqual(content["data"]["pacientes"]["edges"], [])
    
    def test_create_paciente(self):
        query = '''
           mutation {
            createPaciente(
                fecha: "2023-09-09",
                nombre: "Lazaro",
                nombreDeLaMadre: "Juana",
                provincia: "Holguin",
                municipio: "Holguin",
                diagnosticoEgreso: "Bien",
                direccion: "Calle 1",
                alta: VIVO,
            ){
                paciente{
                alta,
                nombre,
                }
            }
            }
        '''
        response = self.make_query(query = query, token = self.superuser_token)
        content = json.loads(response.content)
        self.assertDictEqual(content["data"]["createPaciente"]["paciente"], {"alta":"VIVO", "nombre":"Lazaro"})  
    
    def test_create_paciente_without_give_required_fields_returns_error(self):
        query = '''
           mutation {
            createPaciente(
                fecha:"2023-06-09",
            ){
                paciente{
                alta,
                nombre,
                }
            }
            }
        '''
        response = self.make_query(query = query, token = self.superuser_token)
        self.assertContains(response = response, text = "CreatePacienteMutation.mutate() missing 6 required positional arguments") 
    
    def test_update_paciente(self):
        paciente_id = self.create_paciente()
        query = '''
            mutation updatePaciente($id:ID!){
                updatePaciente(id:$id, nombre:"Ramon", nombreDeLaMadre:"Ramona"){
                    paciente{
                        nombre,
                        nombreDeLaMadre,
                    }
                }
            }
        '''    
        response = self.query(
            query = query,
            headers = {
                "HTTP_AUTHORIZATION":f"JWT {self.superuser_token}",
            },
            variables = {
                "id":paciente_id,
            }
        )
        content = json.loads(response.content)
        self.assertDictEqual(content["data"]["updatePaciente"]["paciente"], {"nombre":"Ramon", "nombreDeLaMadre":"Ramona"})
    
    def test_get_paciente_as_normal_user(self):
        paciente_id = self.create_paciente()
        response = self.get_paciente(paciente_id, self.user_token)
        content = json.loads(response.content)
        self.assertDictEqual(content["data"]["paciente"], {"id":paciente_id})  
    
    def test_get_paciente_as_superuser(self):
        paciente_id = self.create_paciente()
        response = self.get_paciente(paciente_id, self.superuser_token)
        content = json.loads(response.content)
        self.assertDictEqual(content["data"]["paciente"], {"id":paciente_id})      
    
    def test_get_paciente_giving_a_wrong_id(self):
        response = self.get_paciente(paciente_id = "asdasd", token = self.superuser_token)
        self.assertContains(response = response, text = "The given id is not valid")
    
    def test_delete_paciente(self):
        paciente_id = self.create_paciente() 
        response = self.delete_paciente(paciente_id)
        self.assertContains(response = response, text = "Paciente borrado exitosamente")
    
    def test_delete_paciente_giving_a_wrong_id(self):
        response = self.delete_paciente(paciente_id = "asdasd")
        self.assertContains(response = response, text = "The given id is not valid")
    