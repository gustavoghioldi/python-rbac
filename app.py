from eve import Eve
from settings.settings import get_settings
import yaml
from flask import jsonify, request, abort
from models.permission import Permission
from models.user import User
from hooks.fetch import pre_get_callback, pre_delete_callback, pre_post_callback, pre_put_callback

app = Eve(settings=get_settings())

app.on_pre_GET += pre_get_callback
app.on_pre_POST += pre_post_callback
app.on_pre_PUT += pre_put_callback
app.on_pre_DELETE += pre_delete_callback

@app.route('/permissions')
def permissions():
    return jsonify(Permission.get_permissions_names()), 200

@app.route('/jwt')
def is_user():
    users = app.data.driver.db['users']
    try:
        authorization_values = request.authorization
        user = users.find({"username":authorization_values["username"], "password":authorization_values["password"]})
        if user.count() == 1:
            pass
        else:
            raise()
    except Exception as identifier:
        abort(status=401)
    user = User(username=user[0]['username'], merchant=str(user[0]['merchant']), roles=user[0]['roles'])
    user_jwt = user.create_jwt()
    print(user.get_permissions_names())
    print(Permission.get_permissions_names())
    print(Permission.can(user.get_permissions_names(), "auth", "/api/users", "GET"))
    return {"jwt":user_jwt}, 200