from cuentaahorros import cuentaahorros
from cuentacorriente import cuentacorriente
from cdt import cdt


class simuladorbancario:
    # aqui va el codigo
    # atributos
    cedula= ""
    nombre= ""
    mesactual= ""
    """----------------------------------
    #ASOCIACIONES
    ------------------------------------"""
    cuentacorriente = cuentacorriente()
    cuentaahorros = cuentaahorros()
    cdt = cdt()
    """--------------------------
    METODOS"
    -----------------------------"""
    def ConsignarCuentaCorriente(self):
        #aqui va el codigo de la copnsignacion de la cuenta
        return self.ConsignarCuentaCorriente
    
    def CalcularSaldoTotal(self):
        #aqui va el codigo
        return "CalcularSaldoTotal:" +(self.cuentaahorros.saldo + cuentacorriente.saldo + self.cdt.saldo)
    
    
    