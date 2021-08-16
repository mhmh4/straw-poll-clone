from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SubmitField
from wtforms.validators import DataRequired, Length


class PollForm(FlaskForm):
    title = StringField(
        "title", validators=[DataRequired(), Length(min=1, max=400)])
    # allow_multiple_poll_answers = BooleanField("Allow multiple poll answers")
    create_poll = SubmitField("Create Poll")


class VoteForm(FlaskForm):
    ...
