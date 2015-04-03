# -*- coding: utf-8 -*-
from flask import Blueprint, Response

front_module = Blueprint('front', __name__, template_folder='templates')


@front_module.route('/', methods=['GET'])
def index_action():
    return Response('<html><body>Hello world!</body></html>', mimetype="text/html")