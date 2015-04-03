from application import db
from datetime import datetime
from sqlalchemy.ext.hybrid import hybrid_property


class Notes(db.Model):
    __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    title = db.Column(db.String(150))
    body = db.Column(db.String(500))
    date_created = db.Column(db.DateTime(), default=datetime.utcnow)
    date_updated = db.Column(db.DateTime(), onupdate=datetime.utcnow())

    @hybrid_property
    def created(self):
        return self.date_created.strftime('%Y-%m-%d %H:%M:%S.%f')
    
    @hybrid_property
    def modified(self):
        return self.date_updated.strftime('%Y-%m-%d %H:%M:%S.%f')

    # def as_dict(self):
    #     return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}