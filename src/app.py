from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config["SECRET_KEY"] = ...


@app.route("/")
def main():
    return render_template("main.html")


def poll():
    ...


if __name__ == "__main__":
    app.run(debug=True)
