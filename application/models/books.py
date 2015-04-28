# -*- coding: utf-8 -*-
from flask import g
from application import db
from application.models import notes
from datetime import datetime
import uuid


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    guid = db.Column(db.String(32))
    title = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    date_created = db.Column(db.DateTime(), default=datetime.utcnow)
    last_sync = db.Column(db.DateTime())
    notes = db.relationship(notes.Notes, lazy="dynamic")

    def __init__(self, title):
        self.title = title
        self.guid = uuid.uuid4().hex
        # self.user_id = g.user.id
        self.user_id = 3

    def __repr__(self):
        return '<Book %r>' % self.title