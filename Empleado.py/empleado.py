from fecha import fecha

class empleado:
    # aqui va el codigo del empleado
    
    # ATRIBUTOS
    nombre = ""
    apellido = ""
    genero = ""
    # 1= masculino y 2= femenino
    salario = 0
    """-----------------------------------
    # ASOCIACIONES
    ------------------------------------"""
    
    fechaNacimiento=fecha()
    fechaIngreso=fecha()
    
    '''------------------------------------
    # METODOS
    ---------------------------------------'''
    
    def CambiarSalario(self, nuevoSalario):
        # aqui va el codigo del metodo
         return 0

    def cambiarEmpleado(self, nuevoEmpleado):
        # aqui va el codigo del nuevo empleado
         return None
     
    def ConsultarSalario(self):
        # aqui va el codigo del metodo
         return self.saldo
     
    def ConsultarNombre(self):
        # aqui va el codigo del metodo
        return self.nombre

    def ConsultarApellido(self):
        # aqui va el codigo del metodo
        return self.apellido

    def ConsultarNombreCompleto(self):
        # aqui va el codigo del metodo
        return self.nombre +" "+ self.apellido

    def AumentoSalario(self):
        nsalario = self.salario * 0.05
        nsalario = nsalario + self.salario
        self.salario = nsalario
        
    def CambiarNombre(selef, nnombre):
        self.nombre = nnombre
        return "el nuevo nombre es"+self.nombre
    
    def CambiarApellido(self, napellido):
        # aqui va el codidfo del metodo
        self.apellido = napellido
        return "el nuevo apellido es"+self.apellido
    
    def DuplicarSalario(self):
        #aqui va el codigo
         #forma 2 pro
        self.salario *= 2
        
    def CalcularSalarioAnual(self):
        # aqui va el codigo
        #forma 1
        salarioAnual = self.salario*12
        return salarioAnual
    
    def ConsutarDiaCumpleAnios(self):
        return "el dia de cumpleaños es:"+self.fechaNacimiento.consultarDia
    
    def ConsultarImpuesto(self):
        total = self.CalcularSalarioAnual()
        return (total * 19.5) / 100
    
    
    