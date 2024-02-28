class cuentacorriente:
    # aqui va el codigo
    # atributos 
    saldo = 0
    InteresMensual = 0
    
    def ConsignarValor(self):
        nsaldo = self.saldo + 1000
        self.saldo = nsaldo
        return "el nuevo saldo mas el consignado es" + self.saldo
    
    def RetirarValor(self):
        nsaldo = self.saldo - 1000
        self.saldo = nsaldo
        return "el nuevo saldo mas el valor retirado es" + self.saldo
        
        
        
        
        
        