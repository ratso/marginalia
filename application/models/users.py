from application import db
from wtforms.validators import Email
from passlib.apps import custom_app_context as pwd_context


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(254), index=True, nullable=False, unique=True, info={'validators': Email()})
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.SmallInteger, nullable=False, default=1)
    status = db.Column(db.SmallInteger, nullable=False, default=1)
    locale = db.Column(db.String(100), default='ru')
    timezone = db.Column(db.String(100), default='Europe/Moscow')
    last_sync = db.Column(db.DateTime())
    books = db.relationship('Books', backref='users', lazy='dynamic')

    @staticmethod
    def hash_password(password):
        return pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)

    @staticmethod
    def try_login(email, password):
        user = Users.query.filter_by(email=email).first()
        if not user or not user.verify_password(password):
            return False
        return user

    def token(self):
        return '1234567890'

    def __init__(self, email, password):
        self.email = email
        self.password = self.hash_password(password)

    def __repr__(self):
        return '<User %r>' % self.email