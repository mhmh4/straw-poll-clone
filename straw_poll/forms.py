from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional


class PollForm(FlaskForm):
    title = StringField(
        "title", validators=[DataRequired(), Length(min=1, max=400)])
    option1 = StringField("option 1", validators=[DataRequired(), Length(min=1, max=200)])
    option2 = StringField("option 2", validators=[DataRequired(), Length(min=1, max=200)])
    option3 = StringField("option 3", validators=[Optional(), Length(min=1, max=200)])
    option4 = StringField("option 4", validators=[Optional(), Length(min=1, max=200)])
    option5 = StringField("option 5", validators=[Optional(), Length(min=1, max=200)])
    create_poll = SubmitField("Create Poll")


class VoteForm(FlaskForm):
    vote = SubmitField("Vote")
