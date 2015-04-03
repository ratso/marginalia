from functools import wraps
from flask import request, jsonify, g
from application import app,  ResponseException
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature
from application.models import users as model


def validate_token():
    if request.json:
        token = request.json.get('token')
    elif request.args:
        token = request.args.get('token')
    else:
        raise ResponseException('You need to specify your token')
    s = Serializer(app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except SignatureExpired:
        raise ResponseException('Token is expired!')
    except BadSignature:
        raise ResponseException('Invalid token!')
    user = model.Users.query.get(data['id'])
    g.user = user
    return user


def error_response():
    response = jsonify({
        'success': False,
        'message': 'Unauthorized access! Invalid or expired token provided',
        'code': 401})
    response.status_code = 401
    return response


def login_required(fn):
    @wraps(fn)
    def decorated_function(*args, **kwargs):
        if not validate_token():
            raise ResponseException('Unauthorized access! Invalid or expired token provided', 401)
        return fn(*args, **kwargs)
    return decorated_function


def role_required(fn):
    @wraps(fn)
    def decorated_function(*args, **kwargs):
        if g.user.role == 1:
            raise ResponseException(u'Admin role is required for this action')
        return fn(*args, **kwargs)
    return decorated_function