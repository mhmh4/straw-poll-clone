from . import db


class Poll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(400), nullable=False)
    # allows_multiple_poll_answers = db.Column(db.Boolean, nullable=False)


db.create_all()
db.session.commit()
