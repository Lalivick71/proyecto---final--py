import flask
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    persona_titular = lista_de_datos[" dni "]
    return render_template ("home-banking.html",saludo=persona_titular.saludo(),movimiento = persona_titular.obtener_todos_los_movimientos())

if __name__ == '__main__':

    import proceso_cuentas

    lista_de_datos = proceso_cuenta.crear_cuentas()
    app.run(debug=True) 
