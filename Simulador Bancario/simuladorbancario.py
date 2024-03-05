from cuentaahorros import cuentaahorros
from cuentacorriente import cuentacorriente
from cdt import cdt


class simuladorbancario:
    # aqui va el codigo
    # atributos
    cedula= ""
    nombre= ""
    mesactual= ""
    clientebasico= "basico"
    clienteplata= "plata"
    clienteVIP= "VIP"
    """----------------------------------
    #ASOCIACIONES
    ------------------------------------"""
    cuentacorriente = cuentacorriente()
    cuentaahorros = cuentaahorros()
    cdt = cdt()
    """--------------------------
    METODOS"
    -----------------------------"""
    def ConsignarCuentaCorriente(self, valor):
        self.corriente.ConsignarValor(valor)

    def CalcularSaldoTotal(self):
        return self.corriente.ConsultarSaldo()+self.ahorros.ConsultarSaldo()
    
    def PasarAhorrosACorriente(self):
         self.corriente.ConsignarValor(self.ahorros.ConsultarSaldo())
         self.ahorros.RetirarValor(self.ahorros.ConsultarSaldo())

    def ConsultarSaldoCorriente(self):
        return "tu saldo es:"+self.cuentacorriente.ConsultarSaldo()
    
    def DuplicarAhorro(self):
        self.ahorros.ConsignarMonto(self.ahorros.ConsultarSaldo())

    def RetirarTodo(self):
        total = self.CalcularSaldoTotal()
        self.cuentacorriente.RetirarValor(self.cuentacorriente.ConsultarSaldo())
        self.cuentaahorros.retirarvalor(self.cuentaahorros.ConsultarSaldo())
        return "retiraste total:"+total 
    
    def __init__(self,tipocliente):
        #aqui va el tipo de cliente segun el valor recibido
        self.tipocliente=tipocliente
        #aqui inicializamos el tipo de cliente segun el valor
        self.clienteVIP
        self.clienteplata
        self.clientebasico
        
    def CambiarTipoDeCliente(nuevoTipoCliente):
        self.tipoCliente=nuevoTipoCliente
        
    def RetirarMonto(self,monto):
        descuento = monto*0.01
        nuevosaldo = self.saldo -(monto+descuento)
        self.saldo = nuevosaldo