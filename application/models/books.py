# -*- coding: utf-8 -*-
from application import db
from application.models import notes
from datetime import datetime


class Books(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(), default=datetime.utcnow)
    notes = db.relationship(notes.Notes, lazy="dynamic")