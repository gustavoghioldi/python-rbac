schema = {
    'username': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 150,
        'unique': True,
        'regex': "^\S+$",
        'required': True
    },
    'password': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 16,
        'required': True
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
    'roles' : {
        'type': 'list',
        'data_relation': {
            'resource':'roles',
            'field': '_id',
            'embeddable': True
        }
    },
    'metadata': {
        'type': 'dict',
    }
}

domain = {
    'item_title': 'user',
    'additional_lookup': {
        'url': 'regex("[\w\W]*")',
        'field': 'username'
    },
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'resource_methods': ['GET', 'POST'],
    'schema': schema
}