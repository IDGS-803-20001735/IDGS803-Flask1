from flask import Flask, render_template ,request

app = Flask('__main__')

@app.route("/cinepolis")
def cinepolis():
    
    return render_template("forms.html")

@app.route("/store",  methods = ["POST"])
def store():
    
    nombre = request.form.get("txtNombre")
    compradores = int(request.form.get("txtCompradores"))
    boletos = int(request.form.get("txtBoletos"))
    opcion = request.form.get("option")

    span = ""
    
    total = boletos * 12.00

    totalboletos = compradores * 7

    if totalboletos < boletos:
        span = "{} solo puedes comprar 7 boletos por persona".format(nombre)

        descuento = 0
        total = 0

    elif boletos > 5:
        if opcion == 'si':
            
          descuento = total - (total * 0.15)
          descuento = descuento - (descuento * 0.1)
        else:
            descuento = total - (total * 0.15)

    elif boletos >= 3 and boletos <= 5:
        if opcion == 'si':
            
            descuento = total - (total * 0.1)
            descuento = descuento - (descuento * 0.1)
        else:
            descuento = total - (total * 0.1)
    elif boletos <= 2:
        if opcion == 'si':
            
            descuento = total
            descuento = descuento - (descuento * 0.1)
        else:
            descuento = total

    return render_template("forms.html", total = total, descuento = descuento, span = span, nombre = nombre)

if __name__ == '__main__':
    app.run(debug = True)