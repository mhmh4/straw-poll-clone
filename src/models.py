from . import db


class Poll:
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(400), nullable=False)
    options = ...
