from fecha import fecha
from empleado2 import salario

class empleado:
    # aqui va el codigo del empleado
    
     #ATRIBUTOS
    nombre = ""
    apellido = ""
    salario = 0
    sexo = ""
    # 1= masculino y 2= femenino
    NumeroDeHijos=""
   

    """-----------------------------------
    # ASOCIACIONES
    ------------------------------------"""
    
    fechaNacimiento=fecha()
    fechaIngreso=fecha()
    
    '''------------------------------------
    # METODOS
    ---------------------------------------'''
    
    def __init__(self, nombre, apellido, sexo, salario):
        self.nombre = nombre
        self.apellido =apellido
        self.sexo = sexo
        self.salario = salario

    def CambiarSalario(self, nuevoSalario):
        # aqui va el codigo del metodo
         return 0

    def CambiarEmpleado(self, nuevoEmpleado):
        # aqui va el codigo del nuevo empleado
         return None
     
    def ConsultarSalario(self):
        # aqui va el codigo del metodo
         return self.salario
     
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
        
    def CambiarNombre(self, nnombre):
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
    
    def ConsultarNumeroDeHijos(self):
        #aqui va el nunmero de hijos que tiene
        return self.NumeroDeHijos
    
    def CalcularAuxilioEducativo(self, calcularauxilio):
        #aqui va el auxilio educativo que tiene el empleado
        auxilio=self.salario()*self.NumeroDeHijos()
        return self.salario()*0.005
    
    def CalcularAuxilioEducativo(self, calcularauxilio):
        #calcula el auxilio educativo que tiene el empleado
        auxilio=self.salario()*0
        
    def CalcularDiferenciaSalaria(self):
        #calcular diferencia salaria respecto a otro empleado
        deferencia=(self.salarioempleado1-self.salarioempleado2)
    