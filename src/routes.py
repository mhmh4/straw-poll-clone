from flask import Flask, redirect, render_template, url_for

from . import app


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html", title="Straw Poll")


@app.route("/poll/<int:poll_id>", methods=["GET", "POST"])
def poll(poll_id):
    return render_template("poll.html")


@app.route("/poll/<int:poll_id>/r")
def results(poll_id):
    return render_template("results.html")
