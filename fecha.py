__author__= "Juan Sebastian Ibarra Salas"
__License__="GPL"
__Version__="1.0.0"
__Email__="juan.ibarrasalas@campusucc.edu.co"

class fecha:
    # Aqui inicia la declaracion de la clase 
    
    """----------------------------------------------------------------------------------------------
    # Atributos
    ----------------------------------------------------------------------------------------------"""

    dia=0
    mes=0
    anio=0
    fecha=0

    """#--------------------------------------------------------------------------------------------
    #Metodo
    -------------------------------------------------------------------------------------------------#"""

    __method__= "dar dia"
    __parameter__= "Ninguno"
    __return__="dia"
    __description__="Metodo que regresa el dia"
    def dar_dia(self):
        return self.dia

    __method__= "dar mes"
    __parameter__= "Ninguno"
    __return__="mes"
    __description__="Metodo que regresa el mes"
    def dar_mes(self):
        return self.mes

    __method__= "dar anio"
    __parameter__= "Nuevo anio"
    __return__="anio"
    __description__="Metodo que cambia el anio"
    def dar_anio(self):
        return self.anio

    __method__= "dar fecha"
    __parameter__= "Ninguno"
    __return__="la fecha de la clase"
    __description__="Metodo que regresa la fecha digitada por el usuario"
    def dar_fecha(self):

        def Dar_Fecha (self):
            return self.dia+'/'+self.mes+'/'+self.anio


