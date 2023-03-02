from flask import Flask, render_template


app = Flask(__name__)


projects = [
    {
        "name": "Habit tracker app with Python and MongoDB",
        "thumb": "img/habit-tracking.png",
        "hero": "img/habit-tracking-hero.png",
        "categories": ["python", "web"],
        "slug": "habit-tracking",
        "prod": "https://python-web-habittracker.onrender.com/"
    },
    {
        "name": "Micro blog app with Python and MongoDB",
        "thumb": "img/rest-api-docs.png",
        "hero": "img/rest-api-docs.png",
        "categories": ["python", "web"],
        "slug": "microblog",
        "prod": "https://python-web-microblog-k676.onrender.com/"
    },
    {
        "name": "Investments monitoring app",
        "thumb": "img/personal-finance.png",
        "hero": "img/personal-finance.png",
        "categories": ["python", "postgresql", "web"],
        "slug": "personal-finance",
        "prod": "https://docs.google.com/spreadsheets/d/1HHYoVnYiARJF5FpGrdWaXafuiph3TUGHDDtXKRBQOp8"
    }
]

@app.route("/")
def home():
    return render_template("home.html", projects=projects)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")
