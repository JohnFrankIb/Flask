from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    tareas = ["sqlalchemy", "flask", "tkinter"]
    return render_template('index.html', tarea = tareas)

@app.route("/Diana/")
def diana():
    return f"<h1>Te amo</h1>"

if __name__ == '__main__':
    app.run(debug=True)