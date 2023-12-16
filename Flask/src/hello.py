from flask import Flask, render_template
'''
 Tutorial: https://www.youtube.com/watch?v=icbGQxVJB7I&list=LL&index=6
 min: 22:00
'''
app = Flask(__name__)

@app.route("/<name>")
def hello(name):
    return f"<h1>Hola, {name}. </h1>"

@app.route("/Diana/")
def diana():
    return f"<h1>Te amo</h1>"

if __name__ == '__main__':
    app.run()