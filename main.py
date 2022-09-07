from flask import Flask

app = Flask(__name__)


@app.route("/")  # http://127.0.0.1:5000/
def index():
    return "<p>Home, sweet home.</p>"


@app.route("/greet/")
def greet():
    return "<h1>Hello, world!</h1>"


# Dynamic routing
@app.route("/greet/<name>")
def greet_name(name):
    return "<h1>Hello, and welcome back {}!</h1>".format(name)


if __name__ == "__main__":
    app.run()

# set the FLASK_APP env variable to specify how to load the app with:
# $env:FLASK_APP="file_name"
# then run the app with the 'flask run' command
