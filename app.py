from operaciones import operaciones
from flask import Flask

app = Flask(_name_)
@app.route("/")
def hola():
    return "Hola mundo"

@app.route("/suma/<int:val_1>/<int:val_2>")
def suma(val_1, val_2):
    c = Calculadora()
    c.val1 = val_1
    c.val2 = val_2
    c.suma()

@app.route("/resta/<int:val_1>/<int:val_2>")
def resta(val_1, val_2):
    c = Calculadora()
    c.val1 = val_1
    c.val2 = val_2
    c.resta()

@app.route("/multiplicacion/<int:val_1>/<int:val_2>")
def multiplicacion(val_1, val_2):
    c = Calculadora()
    c.val1 = val_1
    c.val2 = val_2
    c.multiplicacion()

@app.route("/operacion/<operador>/<int:val_1>/<int:val_2>")
def operacion(operador,val_1,val_2):
    c = Calculadora()
    c.val1 = val_1
    c.val2 = val_2
    res = 0

    if (operador == "+"):
        res = c.suma()
    elif (operador == "-"):
        res = c.resta()
    elif (operador == "*"):
        res = c.multiplicacion()
    else:
    res = 0

    return render_template('Archivo.html',resultado = res)


if _name_ == '__main__':
    app.run(debug= True)

