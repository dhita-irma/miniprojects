import cs50
import csv

from flask import Flask, jsonify, redirect, render_template, request, url_for

# Configure application
app = Flask(__name__)


# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True

students = ["Henry", "Harry", "Ron"]

@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def post_form():

    # Validate form and alert user if there is an empty field.
    name = request.form.get("fullname")
    email = request.form.get("email")
    dorm = request.form.get("dorm")
    club = request.form.get("club")
    if not name or not email or not dorm or not club:
        return render_template("error.html", message="All field must be filled out.")

    # Write user input into CSV file
    with open("survey.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow((request.form.get("fullname"), request.form.get("email"), request.form.get("dorm"), request.form.get("club")))
    return redirect(url_for("get_sheet"))


@app.route("/sheet", methods=["GET"])
def get_sheet():
    with open("survey.csv", "r") as file:
        reader = csv.reader(file)
        students = list(reader)
        row_count = len(students)
    return render_template("table.html", students=students, row_count=row_count)













































