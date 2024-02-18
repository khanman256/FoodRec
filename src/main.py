from pickletools import read_uint1
from flask import Flask, render_template, redirect, request, session, url_for
from data import *
from collect import *
from dotenv import load_dotenv
import os
from algo import best_choice



load_dotenv("../.env")
app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]


### GLOBAL VARIABLES DEFINED
@app.context_processor
def inject_globals():
    return dict(
        app_name="FoodRecc",
    )


### PAGES
@app.route("/")
def home_page():
    if 'user_id' in session:
        return redirect(url_for('halls_page'))
    return render_template("home.html", session=session)

@app.route("/halls")
def halls_page():
    if 'user_id' not in session:
        return redirect(url_for('home'))

    user = get_user_from_id(session['user_id'])
    food, station, hall = best_choice(user)

    return render_template("halls.html", halls=dining_halls, session=session, recommended=food, recommended_hall=hall, recommended_station=station)
    

@app.route("/halls/<id>")
def hall_info(id):
    if 'user_id' not in session:
        return redirect(url_for('home'))
    hall = get_dining_hall(id)
    return render_template("hall_info.html", hall=hall, session=session)

## REVIEW STUFF
@app.route("/review", methods=["POST"])
def new_review():
    if 'user_id' not in session:
        return redirect(url_for('halls_page'))
    
    food_id = request.form['food_id']
    rating = int(request.form['rating'])
    if user_can_rate_food(session['user_id'], food_id):
        add_rating(session['user_id'], food_id, rating)
        return redirect(url_for('halls_page'))


### AUTH PAGES    
@app.route("/auth/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"].lower()
        password = request.form["password"]
        user = get_user_from_name(username)
        if user and user.validate_password(password):
            session["user_id"] = user.id
            return redirect(url_for("halls_page"))
        return render_template("login.html", error="Incorrect username or password!", session=session)
    else:
        return render_template("login.html", error=None, session=session)

@app.route("/auth/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        username = request.form["username"].lower()
        password = request.form["password"]
        # add the user
        if does_user_exist(username):
            return render_template("create.html", error="Username already exists!", session=session)
        else:
            new_user = User(username)
            new_user.set_password(password)
            add_user(new_user)
        return redirect(url_for("home_page"))
    else:
        return render_template("create.html", error=None, session=session)

@app.route("/auth/logout")
def logout():
    if 'user_id' in session:
        session.pop('user_id', default=None)
    return redirect(url_for('home_page'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001,debug=True)
