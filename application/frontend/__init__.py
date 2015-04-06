# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

front_module = Blueprint('front', __name__, template_folder='templates')


@front_module.route('/', defaults={'page': 'index'})
@front_module.route('/<page>')
def show_action(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)