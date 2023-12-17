from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    cursos = ["sqlalchemy", "flask", "tkinter", "PHP"]
    data = {
        "titulo": "index",
        "bienvenida": "Bienvenido",
        "cursos": cursos,
        "numero_cursos": len(cursos)
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

with app.test_request_context():
    print(url_for("index"))
    print(url_for("diana"))

if __name__ == '__main__':
    app.run(debug=True)