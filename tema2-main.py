from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "!!! Hola mundo !!! - otra cosa"

@app.route("/hola")
def hola():
    return "<h1> Saludos desde Hola</h1>"

@app.route("/nueva")
def nueva():
  return "<h1> Saludos desde Nueva</h1>"

if __name__ == "__main__":
    app.run(debug = True)