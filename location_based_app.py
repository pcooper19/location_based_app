from flask import Flask, render_template, request, session, redirect, url_for
from models import db, User
from forms import SignupForm


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://localhost/learningflask"
db.init_app(app)

app.secret_key = "development=key" # used to protect against Cross sight request forgery (CSRF)

@app.route("/")
def index():
     return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/signup", methods = ["GET", "POST"])

def signup():
    form = SignupForm()

    if request.method == "POST":
        if form.validate() == False: # if we are unable to verify the form data, reload the form
            return render_template("signup.html", form = form)
        else:
            newuser = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
            db.session.add(newuser)
            db.session.commit()

            session["email"] = newuser.email #creates a new session when a new users signs up for the app
            return redirect(url_for("home")) # user is this re-directed to the home page

    elif request.method == "GET":
        return render_template("signup.html", form = form)

@app.route("/home")
def home():
    return render_template("home.html")
    app.run(debug = True)

if __name__ == "__main__":
  app.run(debug = True)