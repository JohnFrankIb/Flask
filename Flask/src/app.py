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




@app.route("/Diana/")
def diana():
    return f"<h1>Te amo</h1>"

if __name__ == '__main__':
    app.run(debug=True)