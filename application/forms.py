from flask.ext.wtf import Form
 
from wtforms_alchemy import model_form_factory
from wtforms import StringField
from wtforms.validators import DataRequired
 
from application import db
from application.models import *
 
BaseModelForm = model_form_factory(Form)


class ModelForm(BaseModelForm):
    @classmethod
    def get_session(cls):
        return db.session


class UserCreateForm(ModelForm):
    class Meta:
        model = Users


class SessionCreateForm(Form):
    email = StringField('email', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])


class BookCreateForm(ModelForm):
    class Meta:
        model = Books


class NotesCreateForm(ModelForm):
    class Meta:
        model = Notes