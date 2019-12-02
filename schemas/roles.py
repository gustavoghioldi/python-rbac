from models.permission import Permission
schema = {
    'name': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 15,
        'unique': True,
        'regex': "^\S+$",
        'required': True
    },
    'permissions':{
        'type': "list",
        'allowed': Permission.get_permissions_names(),
    },
    'merchant': {
        'required': True,
        'type': 'objectid',
        'data_relation': {
            'resource':'merchants',
            'field': '_id',
            'embeddable': True
        }

    },
    'metadata': {
        'type': 'dict',
    }
}

domain = {
    'item_title': 'name',
    'additional_lookup': {
        'url': 'regex("[\w\W]*")',
        'field': 'name'
    },
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'resource_methods': ['GET', 'POST'],
    'schema': schema
}