from werkzeug.security import generate_password_hash, check_password_hash

from App.ext import db
from App.models import BaseModel


class CinemaUser(BaseModel):
    username = db.Column(db.String(32), unique=True)
    _password = db.Column(db.String(256))

    phone = db.Column(db.String(32), unique=True)
    is_delete = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        raise Exception("can't access")

    @password.setter
    def password(self, password_value):
        self._password = generate_password_hash(password_value)

    def check_password(self, password_value):
        return check_password_hash(self._password, password_value)

class Permissions(BaseModel):
    p_name = db.Column(db.String(64), unique=True)

class CinemaUserPermission(BaseModel):
    c_user_id = db.Column(db.Integer, db.ForeignKey(CinemaUser.id))
    c_permission_id = db.Column(db.Integer, db.ForeignKey(Permissions.id))