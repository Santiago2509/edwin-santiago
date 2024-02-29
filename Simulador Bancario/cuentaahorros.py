class cuentaahorros:
    # aqui va el codigo 
    # atributos
    saldo= 0
    interesmensual= 0
    """ # metodos"""
       
    def ConsultarSaldo(self):
        return self.saldo
   
    def consignarvalor(self):
        nsaldo= self.saldo + 1000
        self.saldo= nsaldo
        return "el nuevo saldo mas el consignado es" + self.saldo
    
    def retirarvalor(self):
        nsaldo= self.saldo - 1000
        self.saldo = nsaldo
        return "el nuevo saldo menos el valor retirado es" + self.saldo
    
    def interesmensual(self):
        nsaldo= self.saldo * 0.6
        nsaldo = self.saldo + nsaldo
        self.saldo = nsaldo
        return "el nuevo saldo ms el interes mensual es" + self.saldo
    
        


