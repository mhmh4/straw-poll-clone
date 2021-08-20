from flask import redirect, render_template, request, url_for

from . import app, db
from .forms import PollForm, VoteForm
from .models import Poll
from .utils import get_poll_percentages


@app.route("/", methods=["GET", "POST"])
def home():
    form = PollForm()
    if form.validate_on_submit():
        poll = Poll(title=form.title.data,
                    option1=form.option1.data,
                    option2=form.option2.data,
                    option3=form.option3.data,
                    option4=form.option4.data,
                    option5=form.option5.data,
                    allows_multiple_poll_answers=\
                        (True if request.form.getlist("allow_multiple")
                        else False))
        db.session.add(poll)
        db.session.commit()
        return redirect(url_for("poll", poll_id=poll.id))
    return render_template("home.html", title="Straw Poll", form=form)


@app.route("/poll/<int:poll_id>", methods=["GET", "POST"])
def poll(poll_id):
    poll = Poll.query.get_or_404(poll_id)
    if request.method == "POST":
        value1 = request.form.getlist("option1")
        value2 = request.form.getlist("option2")
        value3 = request.form.getlist("option3")
        value4 = request.form.getlist("option4")
        value5 = request.form.getlist("option5")
        if poll.allows_multiple_poll_answers:
            if value1:
                poll.option1_results += 1
            if value2:
                poll.option2_results += 1
            if value3:
                poll.option3_results += 1
            if value4:
                poll.option4_results += 1
            if value5:
                poll.option5_results += 1
        else:
            if value1:
                poll.option1_results += 1
            elif value2:
                poll.option2_results += 1
            elif value3:
                poll.option3_results += 1
            elif value4:
                poll.option4_results += 1
            elif value5:
                poll.option5_results += 1
        db.session.commit()
        return redirect(url_for("results", poll_id=poll.id))
    form = VoteForm()
    return render_template("poll.html",
                           title=f"{poll.title} - Straw Poll",
                           poll=poll,
                           form=form)


@app.route("/poll/<int:poll_id>/r")
def results(poll_id):
    poll = Poll.query.get(poll_id)
    percentages = get_poll_percentages(poll)
    return render_template("results.html",
                           title=f"{poll.title} - Results - Straw Poll",
                           poll=poll,
                           percentages=percentages)
