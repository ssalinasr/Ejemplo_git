from operaciones import operaciones
from flask import Flask

app = Flask(_name_)
@app.route("/")
def hola():
    return "Hola mundo"

if _name_ == '__main__':
    app.run(debug= True)