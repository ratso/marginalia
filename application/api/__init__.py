# -*- coding: utf-8 -*-
from flask import Blueprint
from flask.ext import restful
from flask_restful import OrderedDict
from resources.users import UserResource, UserListResource

api_module = Blueprint('api', __name__)

api = restful.Api(api_module)


class ApiBaseError(Exception):
    def to_dict(self):
        key_map = {'code': 'status_code', 'description': 'message'}
        return OrderedDict([(key_map.get(k, k), getattr(self, k)) for k in ['code', 'description', 'extras'] if hasattr(self,k) and getattr(self, k)])



api.add_resource(UserListResource, '/users', endpoint='UserListResource')
api.add_resource(UserResource, '/users/<int:id>', endpoint='UserResource')