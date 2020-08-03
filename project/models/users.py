from . import db


class User(db.Model):
    u_id = db.Column(db.Integer, nullable=False,
                     primary_key=True, autoincrement=True)
    u_name = db.Column(db.String, nullable=False)
