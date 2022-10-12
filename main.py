from unicodedata import name
from flask import Flask, render_template, request
import sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['DEBUB'] = True

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bdgrupo6.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route("/", methods= ["GET"])
def principal():
    return render_template("login.html")

@app.route("/index", methods= ["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/login", methods=["post"])
def login():
    if request.method == 'POST':
        usuario = request.form["Usuario"]
        contraseña1 = request.form["inputPassword"]
        with sqlite3.connect("bdgrupo6.db") as con:
            cur = con.cursor()
            cur.execute("insert into login (usuario, password) values (?,?)", [usuario, contraseña1])
            con.commit()
        return render_template("login.html")

@app.route("/registrarse", methods=["POST", "GET"])
def registro():
        if request.method == 'POST':
            correo = request.form["correo"]
            nickname = request.form["nickname"]
            edad = request.form["edad"]
            user = request.form["user"]
            contraseña = request.form["pass"]
            respuesta = request.form["pregunta"]
            with sqlite3.connect("bdgrupo6.db") as con:
                cur = con.cursor()
            cur.execute("insert into registro (correo, nickname, edad, usuario, password, pregunta ) values (?,?,?,?,?,?)",
            [correo, nickname, edad, user,contraseña,respuesta])
            con.commit()
            return render_template("registro.html")
        else:
            return render_template("registro.html")


@app.route("/login/perfil", methods=["GET"])
def perfil():
    return render_template("perfil.html")

@app.route("/login/index/configuraciones", methods= ["GET"])
def configuracion():
    return render_template("configuraciones.html")

@app.route("/login/perfil/configuraciones/informacion", methods= ["GET"])
def información():
    return render_template("informacion.html")
    
@app.route("/login/perfil/configuraciones/cambio-contraseña", methods= ["GET"])
def cambioContrasena():
    return render_template("cambio_contrasena.html")

@app.route("/login/perfil/comentarios", methods= ["GET"])
def comentarios():
    return render_template("comentarios.html")

@app.route("/login/perfil/publicacion", methods= ["GET", "POST"])
def publicacion():
    return render_template("publicacion.html")

@app.route("/index/subir-imagen", methods= ["GET"])
def subirImagen():
    return render_template("subir_imagen.html")

@app.route("/login/perfil/mensajes", methods= ["GET"])
def mensajes():
    return render_template("mensajes.html")

@app.route("/login/perfil/mensajes/nuevo-mensaje", methods= ["GET"])
def nuevoMensaje():
    return render_template("nuevo_mensaje.html")

if __name__ == "__main__":
    app.run(debug=True)



