from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/")
@app.route("/<path:nombre>")
def index(nombre=None):
    print(url_for("index"))
    print(url_for("diana"))
  #  print(url_for("auth/register"))
    cursos = ["sqlalchemy", "flask", "tkinter", "PHP"]
    data = {
        "titulo": "index",
        "bienvenida": "Bienvenido",
        "cursos": cursos,
        "numero_cursos": len(cursos),
        "nombre": nombre
    }

    return render_template('index.html', cursos=cursos, data=data)


@app.route("/diana/")
def diana():
    data={
        "amor": "Te amooo",
        "nombre": "Dianitaaaaa",
        "carac": "chulaaa"
    }
    return render_template("diana.html", data=data)

@app.route("/register/", methods = ["GET", "POST"])
def register():
    
    if request.method == "POST":
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']
        return f'Nombre de usuario {usuario}, contraseña: {contrasena}'

    data = {
        "titulo": "Registrate",

    }

    return render_template("auth/register.html", data=data)


# with app.test_request_context():
#     print(url_for("index"))
#     print(url_for("diana"))

if __name__ == '__main__':
    app.run(debug=True)