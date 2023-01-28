from flask import Flask

app = Flask(__name__)

@app.route("/user/<string:user>")
def user(user):
    return "!!! Hola mundo !!! " + user

@app.route("/number/<int:n>")
def numero(numero):
    return "Numero: {}".format(numero)

@app.route("/user/<int:id>/<string:name>")
def func(id, name):
    return "ID: {} Nombre: {}".format(id, name)

@app.route("/suma/<float:num1>/<float:num2>")
def suma(num1, num2):
    return "La suma es: {}".format(num1 + num2)

@app.route("/age/<int:age>/<string:name>")
def age(name, age):
    return "{} tu edad es : {}".format(name,age)

if __name__ == "__main__":
    app.run(debug = True)