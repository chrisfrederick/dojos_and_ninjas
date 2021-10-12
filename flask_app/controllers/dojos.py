from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.dojo import Dojo

@app.route("/")
def select_dojo():
    dojo = Dojo.get_all_dojos()
    return render_template("index.html", dojo=dojo)


@app.route("/show_dojo/<int:id>")
def show_dojo(id):
    data = {
        "id": id
    }
    dojo = Dojo.get_dojos_ninjas(data)
    return render_template("show_dojo.html", dojo=dojo)


@app.route("/insert_dojo", methods=["POST"])
def insert_dojo():
    data = {
        "name": request.form["name"]
    }
    new_dojo = Dojo.save_dojo(data)
    return redirect("/")

@app.route("/delete_dojo/<int:id>")
def delete_dojo(id):
    data ={
        "id":id
    }
    Dojo.delete_dojo(data)
    return redirect("/")