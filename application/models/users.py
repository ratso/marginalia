from application import db, app
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


class Users(db.Model):
    # __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(254), index=True, nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    # Authorisation Data: role & status
    role = db.Column(db.SmallInteger, nullable=False)
    status = db.Column(db.SmallInteger, nullable=False)
    locale = db.Column(db.String(100), default='ru')
    timezone = db.Column(db.String(100), default='Europe/Moscow')

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self, expiration=3600):
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def try_login(email, password):
        user = Users.query.filter_by(email=email).first()
        if not user or not user.verify_password(password):
            return False
        return user