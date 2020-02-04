import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    return apology("Hompage is under construction")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():

    if request.method == "GET":
        return render_template("buy.html")
    else:
        # Check if the input is valid
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        if not symbol:
            return "Symbol cannot be empty"
        elif not lookup(symbol):
            return "Symbol does not exist"
        elif not shares:
            return "Shares cannot be empty"

        # Add stock to user's portofolio
        price = lookup(symbol)["price"]
        proper_sym = lookup(symbol)["symbol"]
        row = db.execute("SELECT cash FROM users WHERE id = :user_id", user_id = session["user_id"])
        cash = row[0]["cash"]
        if cash >= (price*int(shares)):
            db.execute("INSERT INTO transaction (id, symbol, price, share) VALUES (:user_id, :symbol, :price, :shares)",
                        user_id=session["user_id"], symbol=proper_sym, price=price, shares=int(shares))
            db.execute("UPDATE users SET cash = cash - :spending WHERE id=:user_id", spending=price*int(shares), user_id=session["user_id"])
            return "Your transaction has been recorded"
        else:
            return "You can't afford this stock"

        # Update cash

@app.route("/check", methods=["GET"])
def check():
    """Return true if username available, else false, in JSON format"""
    return jsonify("TODO")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():

    if request.method == "GET":
        return render_template("quote.html")

    else:
        value = lookup(request.form.get("symbol"))
        return render_template("quoted.html", value=value)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via GET (as by clicking a link or via redirect)
    if request.method == "GET":
        return render_template("register.html")

    # User reached route via POST (as by submitting a form via POST)
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Validate username and password fields
        if not username:
            return apology("Username cannot be blank")
        elif not password:
            return apology("Password cannot be blank")
        elif not confirmation:
            return apology("Please confirm your password")
        elif password != confirmation:
            return apology("Password does not match")

        # Check if username is taken, if not insert user to database
        uname_data = db.execute("SELECT * FROM users WHERE username = :username",
                          username=username)
        if not uname_data:
            db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)",
                username=username, hash=generate_password_hash(password))

            # Remember user session
            rows = db.execute("SELECT * FROM users WHERE username = :username",
                              username=username)
            session["user_id"] = rows[0]["id"]
            return redirect("/")

        else:
           return "Username is taken"



@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    return apology("TODO")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
