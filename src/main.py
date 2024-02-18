from flask import Flask, render_template
from data import *
from collect import *

app = Flask(__name__)


### GLOBAL VARIABLES DEFINED
@app.context_processor
def inject_globals():
    return dict(
        app_name="FoodRecc"
    )


### PAGES
@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/halls")
def halls_page():
    return render_template("halls.html", halls=dining_halls)

@app.route("/halls/<id>")
def hall_info(id):
    dining_hall = get_dining_hall(id)
    return render_template("hall_info.html", hall=dining_hall)


### AUTH PAGES    
@app.route("/auth/login")
def login():
    return render_template("login.html")

@app.route("/auth/create")
def create():
    return render_template("create.html")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001,debug=True)
