from flask import Flask, redirect, request, render_template, session
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions
app.secret_key = "DEV"

# The top melons at Ubermleon
MOST_LOVED_MELONS = {
    "cren": {
        "img": "http://www.rareseeds.com/assets/1/14/DimRegular/crenshaw.jpg",
        "name": "Crenshaw",
        "num_loves": 584,
    },
    "jubi": {
        "img": "http://www.rareseeds.com/assets/1/14/DimThumbnail/Jubilee-Watermelon-web.jpg",
        "name": "Jubilee Watermelon",
        "num_loves": 601,
    },
    "sugb": {
        "img": "http://www.rareseeds.com/assets/1/14/DimThumbnail/Sugar-Baby-Watermelon-web.jpg",
        "name": "Sugar Baby Watermelon",
        "num_loves": 587,
    },
    "texb": {
        "img": "http://www.rareseeds.com/assets/1/14/DimThumbnail/Texas-Golden-2-Watermelon-web.jpg",
        "name": "Texas Golden Watermelon",
        "num_loves": 598,
    },
}


@app.route("/top-melons")
def show_top_melons():
    """Display info of melons in MOST_LOVED_MELONS."""

    if "name" not in session:
        return redirect("/")

    return render_template("top-melons.html", melons=MOST_LOVED_MELONS)


@app.route("/")
def show_homepage():
    """Show homepage."""

    if "name" in session:
        return redirect("/top-melons")

    return render_template("homepage.html")


@app.route("/get-name")
def get_name():
    """Get name and store in session."""

    name = request.args.get("name")
    print('\n')
    print("*" * 20)
    print("name is", name)

    if name != None:
        session["name"] = name
        print('\n')
        print("*" * 20)
        print("session is", session)
        print("*" * 20)
        print('\n')

    return redirect("/top-melons")


@app.route("/love-melon", methods=["POST"])
def process_love_melon():
    """Process form submission to love a melon."""

    melon_id = request.form.get("melon")
    print('\n')
    print("*" * 20)
    print("melon_id is", melon_id)
    print("*" * 20)
    print('\n')

    if melon_id in MOST_LOVED_MELONS:
        MOST_LOVED_MELONS[melon_id]["num_loves"] += 1
        print('\n')
        print("*" * 20)
        print("num_loves is", MOST_LOVED_MELONS[melon_id]["num_loves"])
        print("*" * 20)
        print('\n')

    return render_template("thank-you.html")


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        use_reloader=True,
        use_debugger=True,
    )
