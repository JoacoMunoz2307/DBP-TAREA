from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    name=request.form.get("nombre")
    date=request.form.get("fecha")
    place=request.form.get("lugar")
    sex=request.form.get("genero")
    password=request.form.get("contraseña")
    email=request.form.get("correo")
    married=request.form.get("casado")
    career=request.form.get("carrera")

    return render_template(
        "session.html",
        nombre=name,
        fecha=date,
        lugar=place,
        genero=sex,
        contraseña=password,
        correo=email,
        casado=married,
        carrera=career,
    )
