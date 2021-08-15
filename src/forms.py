from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.core import BooleanField
from wtforms.validators import DataRequired


class CreatePollForm(FlaskForm):
    title = StringField("title", validators=[DataRequired()])
    # options = ...
    allow_multiple_poll_answers = BooleanField("Allow multiple poll answers")
    create_poll = SubmitField("Create poll")


class VotePollForm(FlaskForm):
    ...
