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
#app.jinja_env.filters["usd"] = usd
app.jinja_env.globals.update(usd=usd)

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

    user_id = session["user_id"]
    purchases = db.execute(
        "SELECT symbol, SUM(share) FROM purchases WHERE id = :user_id GROUP BY symbol HAVING SUM(share) > 0", user_id=user_id)
    cash = db.execute("SELECT cash FROM users WHERE id = :user_id", user_id=user_id)[0]["cash"]

    # List of all stocks owned by the user {name: name, price: price, symbol: symbol}
    stocks = []
    for purchase in purchases:
        stocks.append(lookup(purchase["symbol"]))

    # Number of items in [stocks]
    len_stocks = len(stocks)

    # Total value of stocks
    total_value = 0
    for i in range(len_stocks):
        total_value += purchases[i]["SUM(share)"] * stocks[i]["price"]

    return render_template("index.html", stocks=stocks, len_stocks=len_stocks, total_value=total_value, cash=cash, purchases=purchases)


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
            return apology("Symbol cannot be empty")
        elif not lookup(symbol):
            return apology("Symbol does not exist")
        elif not shares:
            return apology("Shares cannot be empty")
        elif shares.isdigit() == False:
            return apology("Number of share is invalid")
        elif int(shares) < 0:
            return apology("Number of share is invalid")

        # Add stock to user's portofolio
        shares = int(shares)
        price = lookup(symbol)["price"]
        proper_sym = lookup(symbol)["symbol"]
        name = lookup(symbol)["name"]
        row = db.execute("SELECT cash FROM users WHERE id = :user_id", user_id=session["user_id"])
        cash = row[0]["cash"]
        if cash >= (price*shares):
            db.execute("INSERT INTO purchases (id, symbol, price, share) VALUES (:user_id, :symbol, :price, :shares)",
                       user_id=session["user_id"], symbol=proper_sym, price=price, shares=shares)
            db.execute("UPDATE users SET cash = cash - :spending WHERE id=:user_id",
                       spending=price*shares, user_id=session["user_id"])
            return redirect("/")
        else:
            return apology("You don't have enough cash")


@app.route("/check", methods=["GET"])
def check():
    """Return true if username available, else false, in JSON format"""
    username = request.args.get("username")

    uname_data = db.execute("SELECT * FROM users WHERE username = :username", username=username)

    if len(username) > 1 and not uname_data:
        return jsonify(True)
    else:
        return jsonify(False)


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]
    purchases = db.execute("SELECT symbol, share, price, date FROM purchases WHERE id = :user_id", user_id=user_id)

    # Number of transaction by current user
    purchases_count = db.execute("SELECT COUNT(*) FROM purchases WHERE id = :user_id", user_id=user_id)[0]["COUNT(*)"]

    return render_template("history.html", purchases=purchases, purchases_count=purchases_count)


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
            return apology("Invalid username and/or password", 403)

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

    # User reach route via GET
    if request.method == "GET":
        return render_template("quote.html")

    # User reach route via POST
    else:
        value = lookup(request.form.get("symbol"))
        if not value:
            return apology("Invalid symbol")
        else:
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
            return apology("Username is taken")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    user_id = session["user_id"]
    if request.method == "GET":
        purchases = db.execute(
            "SELECT symbol, SUM(share) FROM purchases WHERE id = :user_id AND share > 0 GROUP BY symbol", user_id=user_id)
        return render_template("sell.html", purchases=purchases)

    else:
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))

        # Ensure that user input is valid
        if not symbol:
            return apology("Stock cannot be empty")
        if not shares:
            return apology("Shares cannot be empty")
        if int(shares) > db.execute("SELECT SUM(share) FROM purchases WHERE id = :user_id GROUP BY symbol HAVING symbol = :symbol", user_id=user_id, symbol=symbol)[0]["SUM(share)"]:
            return apology("You don't have enough share")

        price = lookup(symbol)["price"]

        # Add transaction to 'purchases' table
        db.execute("INSERT INTO purchases (id, symbol, price, share) VALUES (:user_id, :symbol, :price, :shares)",
                   user_id=user_id, symbol=symbol, price=price, shares=-shares)

        # Update user's cash
        db.execute("UPDATE users SET cash = cash + :sold WHERE id=:user_id", sold=price*shares, user_id=user_id)

        return redirect("/")


@app.route("/account", methods=["GET", "POST"])
@login_required
def account():
    """Change password"""

    user_id = session["user_id"]

    # User reached route via GET (as by clicking a link or via redirect)
    if request.method == "GET":
        return render_template("account.html")

    # User reached route via POST (as by submitting a form via POST)
    else:
        old_pass = request.form.get("oldPassword")
        new_pass = request.form.get("newPassword")
        confirmation = request.form.get("confirmation")

        current_pass = db.execute("SELECT hash FROM users WHERE id = :user_id", user_id=user_id)[0]["hash"]

        if check_password_hash(current_pass, old_pass):
            if new_pass == confirmation:
                db.execute("UPDATE users SET hash = :new_pass WHERE id = :user_id",
                           new_pass=generate_password_hash(new_pass), user_id=user_id)
                return render_template("pass.html", message="Password has been changed successfully")
            else:
                return render_template("pass.html", message="New password does not match")
        else:
            return render_template("pass.html", message="Old password is invalid")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
