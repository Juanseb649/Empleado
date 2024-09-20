__author__= "Juan Sebastian Ibarra Salas"
__License__="GPL"
__Version__="1.0.0"
__Email__="juan.ibarrasalas@campusucc.edu.co"

from fecha import fecha

class Empleado:
    # Aqui inicia la declaracion de mi clase
    """----------------------------------------------------------------------------------------------
    # Atributos
    ----------------------------------------------------------------------------------------------"""
    Nombre=""
    Apellido=""
    Salario=0
    """#--------------------------------------------------------------------------------------------
    #1=Masculino,#2= Femenino
    ---------------------------------------------------------------------------------------------#"""
    Sexo=0 
    """#--------------------------------------------------------------------------------------------
    # Asociacion
    -------------------------------------------------------------------------------------------------#"""
    Fecha_Ingreso= fecha()
    Fecha_Nacimiento= fecha()
    """#--------------------------------------------------------------------------------------------
    # Metodo
    -------------------------------------------------------------------------------------------------#"""
    def Dar_nombre(self):
        __method__ = "cambiarsalario"
    __parameter__= "NuevoSalario"
    __return__="salario"
    __description__="Metodo acualiza el salario del empleado"
    def Cambiar_salario (self, nuevosalario):
        self.salario= nuevosalario
        return self.salario
    
    def Dar_salario(self):
        return self.salario
    def consultar_Fecha_ingreso(self):
            return self.Fecha_Ingreso.Dar_Fecha()
    __method__ = "Calcular Salario Anual"
    __parameter__= "Ninguno"
    __return__="salario anual"
    __description__="Metodo el salario anual del empleado"
    def calcular_salario_anual(self):
        total= self.salario*12
        return total
        return self.salario*12
    __method__ = "Calcular impuesto salario anual"
    __parameter__= "Ninguno"
    __return__="Impuesto del salario anual"
    __description__="Muestra el impuesto del salario anual del empleado"
def calcular_impuestos_salario_anual(self):
        
        salario_anual=self.calcular_salario_anual()
        impuesto_anual=salario_anual*0.19
        return impuesto_anual
        return self.calcular_salario_anual()*0.19
        return self.salario()*0.19