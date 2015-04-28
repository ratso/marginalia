# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

front_module = Blueprint('front', __name__, template_folder='templates')


@front_module.route('/')
def show_action():
    try:
        return render_template('pages/index.html')
    except TemplateNotFound:
        abort(404)


@front_module.route('partial/<page>.tpl')
def show_partials_action(page):
    try:
        return render_template('partials/%s.html' % page)
    except TemplateNotFound:
        abort(404)