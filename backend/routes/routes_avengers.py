import os
from flask import Blueprint, request, render_template, redirect
from backend.models.avengers import Avenger
from backend.models.db import db
from werkzeug.utils import secure_filename

avenger_bp = Blueprint('avenger_bp', __name__)

@avenger_bp.route("/", methods=["GET"])
def home():
    avengers = Avenger.query.all()
    return render_template("index.html", avengers=avengers)

# @avenger_bp.route("/api/avengers", methods=["GET"])
# def api_get_all():
#     return jsonify([a.serialize() for a in Avenger.query.all()])

# @avenger_bp.route("/api/avengers/<string:avenger_id>", methods=["GET"])
# def api_get_by_id(avenger_id):
#     avenger = Avenger.query.get(avenger_id)
#     if avenger:
#         return jsonify(avenger.serialize())
#     return jsonify({"error": "Avenger no encontrado"}), 404

# @avenger_bp.route("/api/avengers", methods=["POST"])
# def avenger_create():
#     data = request.json
#     new_avenger = Avenger(
#         nombre=data["nombre"],
#         alias=data["alias"],
#         habilidades=data["habilidades"],
#         actor=data["actor"]
#     )
#     db.session.add(new_avenger)
#     db.session.commit()
#     return jsonify(new_avenger.serialize()), 201

# @avenger_bp.route("/api/avengers/<string:avenger_id>", methods=["PUT"])
# def avenger_update(avenger_id):
#     avenger = Avenger.query.get(avenger_id)
#     if not avenger:
#         return jsonify({"error": "Avenger no encontrado"}), 404
#     data = request.json
#     avenger.nombre = data["nombre"]
#     avenger.alias = data["alias"]
#     avenger.habilidades = data["habilidades"]
#     avenger.actor = data["actor"]
#     db.session.commit()
#     return jsonify(avenger.serialize())

# @avenger_bp.route("/api/avengers/<string:avenger_id>", methods=["DELETE"])
# def avenger_delete(avenger_id):
#     avenger = Avenger.query.get(avenger_id)
#     if not avenger:
#         return jsonify({"error": "Avenger no encontrado"}), 404
#     db.session.delete(avenger)
#     db.session.commit()
#     return jsonify({"message": "Avenger eliminado"})

@avenger_bp.route("/new", methods=["GET", "POST"]) #para crear avenger desde el formulario 
def new_avenger():
    if request.method == "POST":
        nombre = request.form["nombre"]
        alias = request.form["alias"]
        habilidades = request.form["habilidades"]
        actor = request.form["actor"]

        
        new_avenger = Avenger(
            nombre=nombre,
            alias=alias,
            habilidades=habilidades,
            actor=actor
        )

        db.session.add(new_avenger)
        db.session.commit()
        return redirect("/")

    return render_template("new_avenger.html")

@avenger_bp.route("/delete/<string:avenger_id>", methods=["POST"])
def delete_avenger_form(avenger_id):
    avenger = Avenger.query.get(avenger_id)
    if not avenger:
        return "Avenger no encontrado", 404

    db.session.delete(avenger)
    db.session.commit()
    return redirect("/")

@avenger_bp.route("/edit/<string:avenger_id>", methods=["GET", "POST"])
def edit_avenger(avenger_id):
    avenger = Avenger.query.get(avenger_id)
    if not avenger:
        return "Avenger no encontrado", 404

    if request.method == "POST":
        avenger.nombre = request.form["nombre"]
        avenger.alias = request.form["alias"]
        avenger.habilidades = request.form["habilidades"]
        avenger.actor = request.form["actor"]

        
        db.session.commit()
        return redirect("/")

    return render_template("edit_avenger.html", avenger=avenger)

