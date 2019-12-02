import os
from schemas.merchant import domain as merchants
from schemas.user import domain as users
from schemas.roles import domain as roles

def get_settings():
    return  {
    'MONGO_HOST': os.environ['MONGO_HOST'],
    'MONGO_DBNAME': os.environ['MONGO_DBNAME'],
    'RESOURCE_METHODS' : ['GET', 'POST'],
    'ITEM_METHODS' : ['GET', 'PATCH', 'PUT', 'DELETE'],
    'DOMAIN': {
        'merchants': merchants,
        'users': users,
        'roles': roles,
        }
}