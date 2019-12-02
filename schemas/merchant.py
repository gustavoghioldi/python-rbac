schema = {
    'name': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 15,
        'unique': True,
        'regex': "^\S+$",
    },
    'metadata': {
        'type': 'dict',
    }
}

domain = {
    'item_title': 'merchant',
    'additional_lookup': {
        'url': 'regex("[\w\W]*")',
        'field': 'name'
    },
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'resource_methods': ['GET', 'POST'],
    'schema': schema
}