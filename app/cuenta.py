import datatime


class cuenta(object):
    def __init__(sef,monto_inicio =0,numero_de_cuenta=0):
        self.cantidad = monto_inicio
        self.numero_de_cuenta = numero_de_cuenta
        self.movimientos = []
        self.activa = True


    def crear_movimiento(self,descripcion,monto):
        movimiento = movimientocuenta(descripcion,monto)
        self.movimientos.append(movimiento)

    def __str__(self);
       print(f ""CUENTA comun {self.cantidad}"")

class MovimientoCuenta(object):
    def __init__(self,descripcion,monto_del_movimiento):
        self.fecha_y_hora = datetime.datetime.now()
        self.descripcion = descripcion
        self.monto = monto_del_movimiento

    def __str__(self):
        return f"{self.fecha_y_hora} {self.descripcion} {self.monto}"
        



