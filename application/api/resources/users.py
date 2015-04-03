# -*- coding: utf-8 -*-
from flask.ext import restful
from application import db
from application.models import users
from flask.ext.restful import fields, reqparse, marshal, abort
from flask.ext.babel import gettext, get_locale
import re

fields = {
    'id': fields.Integer,
    'email': fields.String,
    'status': fields.Integer,
    'role': fields.Integer,
}


class UserResource(restful.Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('email', type=str, location='json')
        self.reqparse.add_argument('password', type=str, location='json')
        super(UserResource, self).__init__()

    def get(self):
        users_list = db.session.query(users.Users).all()
        return {'success': True, 'users': [marshal(user, fields) for user in users_list]}

    def put(self):
        pass

    def delete(self, id):
        pass


# UserList
#   shows a list of all users, and lets you POST to add new users
class UserListResource(restful.Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('email', type=str, location='json')
        self.reqparse.add_argument('password', type=str, location='json')
        super(UserListResource, self).__init__()

    def get(self):
        users_list = db.session.query(users.Users).all()
        return {'success': True, 'users': [marshal(user, fields) for user in users_list]}

    def post(self):
        args = self.reqparse.parse_args()
        email = args['email']
        password = args['password']
        if email is None or password is None:
            abort(http_status_code=410, message=gettext(u'You need to specify email and password'))
        if not re.match("^[a-zA-Z0-9._%-]+@[a-zA-Z0-9._%-]+.[a-zA-Z]{2,6}$", email):
            raise ValueError(gettext(u'Invalid email address'))
        if users.Users.query.filter_by(email=email).first() is not None:
            raise ValueError(gettext(u'This email is already registered'))
        if len(password) <= 6:
            abort(400, message=gettext(u'Your password is too short. It must be at least 6 characters long!'))
        if password.islower() or password.isupper() or password.isdigit():
            raise ValueError(gettext(u'Password is too week. Use upper and lower registries, digits and symbols'))
        user = users.Users(email=email)
        user.hash_password(password)
        user.role = 1  # Simple user by default
        user.status = 1  # TODO: Authorized by default, need to add confirmation
        if get_locale():
            user.locale = get_locale().language
        db.session.add(user)
        db.session.commit()
        return {'success': True, 'data': marshal(user, fields)}