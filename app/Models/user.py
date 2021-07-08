from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class SecUsers(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    full_name = db.Column(db.String(250), nullable=True)
    username = db.Column(db.String(250), nullable=True)
    email = db.Column(db.String(60), index=True, unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    verification = db.Column(db.Integer, nullable=False, default='0')
    rememberToken = db.Column(
        db.String(250),
        nullable=True,
        unique=True,
    )
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.String(250), nullable=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_by = db.Column(db.String(250), nullable=True)
    deleted_at = db.Column(db.DateTime, default=datetime.utcnow)
    deleted_by = db.Column(db.String(250), nullable=True)

    def __repr__(self):
        return '<SecUsers {}>'.format(self.name)

    def setPassword(self, password):
        self.password = generate_password_hash(password)

    def checkPassword(self, password):
        return check_password_hash(self.password, password)
