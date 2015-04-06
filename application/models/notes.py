from flask import g
from application import db
from datetime import datetime
from sqlalchemy.ext.hybrid import hybrid_property
import uuid


class Notes(db.Model):
    __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True)
    guid = db.Column(db.String(32))
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    title = db.Column(db.String(150))
    body = db.Column(db.String(500))
    date_created = db.Column(db.DateTime(), default=datetime.utcnow)
    date_updated = db.Column(db.DateTime(), onupdate=datetime.utcnow())
    last_sync = db.Column(db.DateTime())

    def __init__(self, title, body, book_id):
        self.title = title
        self.body = body
        self.guid = uuid.uuid4().hex
        self.book_id = book_id

    def __repr__(self):
        return '<Note %r>' % self.title

    @hybrid_property
    def created(self):
        return self.date_created.strftime('%Y-%m-%d %H:%M:%S.%f')
    
    @hybrid_property
    def modified(self):
        return self.date_updated.strftime('%Y-%m-%d %H:%M:%S.%f')

    # def as_dict(self):
    #     return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}