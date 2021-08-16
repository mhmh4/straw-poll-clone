from flask import flash, redirect, render_template, url_for

from . import app, db
from .forms import PollForm
from .models import Poll


@app.route("/", methods=["GET", "POST"])
def home():
    form = PollForm()
    if form.validate_on_submit():
        poll = Poll(title=form.title.data)
        db.session.add(poll)
        db.session.commit()
        return redirect(url_for("poll", poll_id=poll.id))
    return render_template("home.html", title="Straw Poll", form=form)


@app.route("/poll/<int:poll_id>", methods=["GET", "POST"])
def poll(poll_id):
    poll = Poll.query.get_or_404(poll_id)
    return render_template("poll.html",
                           title=f"{poll.title} - Straw Poll",
                           poll=poll)


@app.route("/poll/<int:poll_id>/r")
def results(poll_id):
    poll = Poll.query.get(poll_id)
    return render_template("results.html",
                           title=f"{poll.title} - Results - Straw Poll",
                           poll=poll)
