import datetime
from exts import db


class Authority(db.Model):
    __tablename__ = "authority"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    authority = db.Column(db.String(20), unique=True)


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rid = db.Column(db.Integer, db.ForeignKey('authority.id'))
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    mobile = db.Column(db.String(11), unique=True, nullable=True)
    email = db.Column(db.String(32), unique=True, nullable=True)
    create_time = db.Column(db.DateTime, default=datetime.datetime.now())
    mg_state = db.Column(db.Boolean, default=True)
    # r = relationship("Authority", backref="authority")

    def __str__(self):
        return self.username
