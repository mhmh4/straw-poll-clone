from . import db


class Poll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(400), nullable=False)

    option1 = db.Column(db.String(200), nullable=False)
    option1_results = db.Column(db.Integer, default=0, nullable=False)

    option2 = db.Column(db.String(200), nullable=False)
    option2_results = db.Column(db.Integer, default=0, nullable=False)

    option3 = db.Column(db.String(200), default=None, nullable=True)
    option3_results = db.Column(db.Integer, default=0, nullable=True)

    option4 = db.Column(db.String(200), default=None, nullable=True)
    option4_results = db.Column(db.Integer, default=0, nullable=True)

    option5 = db.Column(db.String(200), default=None, nullable=True)
    option5_results = db.Column(db.Integer, default=0, nullable=True)

    allows_multiple_poll_answers = db.Column(db.Boolean(), nullable=False)


db.create_all()
db.session.commit()
