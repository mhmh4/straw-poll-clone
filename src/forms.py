from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class PollForm(FlaskForm):
    question = StringField("question", validators=[DataRequired()])
    _ = ...
    allows_multiple_answers = ...#BooleanField()
    submit = SubmitField("c")
