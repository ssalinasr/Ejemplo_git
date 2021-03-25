from operaciones import operaciones
from flask import Flask

app = Flask(_name_)
@app.route("/")
def hola():
    return "Hola mundo"

@app.route("/suma/<val_1>/<val_2>")
def suma(val_1, val_2):
    c = Calculadora()
    c.val1 = val_1
    c.val2 = val_2
    c.suma()

if _name_ == '__main__':
    app.run(debug= True)

