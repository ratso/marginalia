# -*- coding: utf-8 -*-
from flask import Blueprint, g
from flask.ext import restful
#from flask.ext.bcrypt import Bcrypt
from flask.ext.httpauth import HTTPBasicAuth
from application.models import Users, Books, Notes
from application import db
from application import forms
from application import serializers

api_module = Blueprint('api', __name__)

api = restful.Api(api_module)

# flask-bcrypt
#flask_bcrypt = Bcrypt(api_module)

auth = HTTPBasicAuth()


@api_module.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


@auth.verify_password
def verify_password(email, password):
    user = Users.try_login(email, password)
    if not user:
        return False
    g.user = user
    return user


class UserView(restful.Resource):
    def post(self):
        form = forms.UserCreateForm()
        if not form.validate_on_submit():
            return form.errors, 422

        user = Users(form.email.data, form.password.data)
        db.session.add(user)
        db.session.commit()
        return serializers.UserSerializer(user).data


class SessionView(restful.Resource):
    def post(self):
        form = forms.SessionCreateForm()
        if not form.validate_on_submit():
            return form.errors, 422

        user = Users.try_login(form.email.data, form.password.data)
        if user:
            return serializers.UserSerializer(user).data, 201
        return '', 401


class BookListView(restful.Resource):
    @auth.login_required
    def get(self):
        books = Books.query.filter_by(user_id=g.user.id).order_by(Books.date_created.desc()).all()
        return serializers.BookSerializer(books, many=True).data

    @auth.login_required
    def post(self):
        form = forms.BookCreateForm()
        if not form.validate_on_submit():
            return form.errors, 422
        book = Books(form.title.data)
        db.session.add(book)
        db.session.commit()
        return serializers.BookSerializer(book).data, 201


class NoteListView(restful.Resource):
    @auth.login_required
    def get(self, book_id):
        notes = Notes.query.filter_by(book_id=book_id).order_by(
            Notes.date_updated.desc(),
            Notes.date_created.desc()
        ).all()
        return serializers.NoteSerializer(notes).data


class NoteView(restful.Resource):
    @auth.login_required
    def post(self):
        form = forms.NotesCreateForm()
        if not form.validate_on_submit():
            return form.errors, 422
        note = Notes(form.title.data, form.body.data, form.book_id.data)
        db.session.add(note)
        db.session.commit()
        return serializers.NoteSerializer(note).data, 201

    @auth.login_required
    def get(self, note_id):
        notes = Notes.query.filter_by(id=note_id).first()
        return serializers.NoteSerializer(notes).data

api.add_resource(UserView, '/users')
api.add_resource(SessionView, '/sessions')
api.add_resource(BookListView, '/books')
api.add_resource(NoteListView, '/notesByBook/<int:book_id>')
api.add_resource(NoteView, '/notes/<int:note_id>')