import jwt
import os
import app
from bson import ObjectId
from models.permission import Permission
class User:
    def __init__(self ,username=None, merchant=None, roles=None, user_jwt=None):    
        if username and merchant and roles and not user_jwt:
            self.properties = {
                "username": username,
                "merchant": merchant,
                "roles": roles
            }
        elif user_jwt:
            self.user_jwt = user_jwt
            self._jwt_decode()
        
    def create_jwt(self):
        self.user_jwt = jwt.encode(self.properties, os.environ['JWT_KEY'], algorithm="HS256").decode('utf-8')
        return self.user_jwt 

    def _jwt_decode(self):
        user = jwt.decode(self.user_jwt, os.environ['JWT_KEY'])
        self.properties = user
    
    def get_objects_roles(self):
        roles = app.app.data.driver.db['roles']
        roles_list = [ObjectId(i) for i in self.properties['roles']]
        rs = roles.find({"_id":{"$in":roles_list}})
        if len(roles_list) != rs.count():
            raise()
        return list(rs)
        
    
    def get_merchant(self):
        merchants = app.app.data.driver.db['merchants']
        merchant = merchants.find({"_id": ObjectId(self.properties['merchant'])})
        if merchant.count() == 1:
            return merchant[0]
        else:
            return False

    def get_permissions_names(self):
        return [i['permissions'] for i in self.get_objects_roles()][0]
        