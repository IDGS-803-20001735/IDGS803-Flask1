from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/operationBasic", methods = ["GET", "POST"])
def operar():
    if request.method == "POST":
        
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        option = request.form.get("option")

        if(option == "sumar"):
            return "<h1> El resultado de la suma es: {} </h1>".format(str(int(num1) + int(num2)))
        elif(option == "restar"):
            return "<h1> El resultado de la resta es: {} </h1>".format(str(int(num1) - int(num2)))
        elif(option == "multiplicar"):
            return "<h1> El resultado multiplicación es: {} </h1>".format(str(int(num1) * int(num2)))
        elif(option == "dividir"):
            return "<h1> El resultado de la divición es: {} </h1>".format(str(int(num1) / int(num2)))
    else:
        return '''
            <form action="/operationBasic" method="POST">
                <label>Número uno:</label><br>
                <input type="text" name="num1"><br>
                <label>Número dos:</label><br>
                <input type="text" name="num2"><br>
                <br>
                <label>Sumar:</label>
                <input type="radio" name="option" value="sumar">
                <br><br>
                <label>Restar:</label>
                <input type="radio" name="option" value="restar">
                <br><br>
                <label>Multiplicar:</label>
                <input type="radio" name="option" value="multiplicar">
                <br><br>
                <label>Dividir:</label>
                <input type="radio" name="option" value="dividir">
                <br><br>
                <input type="submit" value="Calcular">
            </form> 
        '''
if __name__ == "__main__":
    app.run(debug = True)