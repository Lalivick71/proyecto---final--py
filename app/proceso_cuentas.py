import csv

from persona import Persona

def crear_cuentas():

    personas = {}
    archivo = open("personas.csv", "r")

    archivo_csv = csv.reader(archivo)
    next(archivo_csv)
    for nombre,dni,fecha_nacimiento in archivo_csv:
        persona.crear_cuenta()

        personas["dni"] = persona

    archivo.close()
    print (f" {personas}")
    return personas



