from flask_app import app
from flask import redirect, request, render_template, session
from flask_app.models import dojo
from flask_app.models.ninja import Ninja


@app.route("/insert_ninja")
def insert_ninja():
    dojos = dojo.Dojo.get_all_dojos()
    return render_template("add_ninja.html", dojos=dojos)



@app.route("/save_ninja", methods=["POST"])
def save_ninja():
    data = {
        "dojo_id":request.form["dojo"],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age":request.form["age"]
    }
    Ninja.save_ninja(data)
    return redirect("/show_dojo"+str(data["dojo.id"]))