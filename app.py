import flask

app = flask.Flask(__name__)

@app.route("/")#homepage
def home():
    return flask.render_template("base.html", title = "DEO Server")

if __name__ == "__main__":
    app.run(debug=True)