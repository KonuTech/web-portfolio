from flask import Blueprint, render_template, abort


pages = Blueprint(
    "pages", __name__, template_folder="templates", static_folder="static"
)


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
        "prod": "https://docs.google.com/spreadsheets/d/1_q11caQVRR7T2tfqKfYYE2jHgTz5tz007A3hxmLOevI"
    }
]

slug_to_project = {project["slug"]: project for project in projects}


@pages.route("/")
def home():
    return render_template("home.html", projects=projects)


@pages.route("/about")
def about():
    return render_template("about.html")


@pages.route("/contact")
def contact():
    return render_template("contact.html")


@pages.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(
        f"project_{slug}.html",
        project=slug_to_project[slug]
    )

@pages.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404
