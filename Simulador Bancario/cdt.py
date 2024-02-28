class cdt:
    # aqui va el codigo del cdt
    # atributos
    valorinversion= 0
    interesmensual= 0
    mesapertura= 0
    
    def InteresMensual(self):
        nSaldo = self.saldo * 0.0
        nSaldo = self.saldo + nSaldo
        self.saldo = nSaldo
        return "su interes mensual es" + self.saldo